using global::System.Text.Json;
using ZerogpuApi.Core;

namespace ZerogpuApi;

public partial class ResponsesClient : IResponsesClient
{
    private readonly RawClient _client;

    internal ResponsesClient(RawClient client)
    {
        _client = client;
    }

    private async Task<WithRawResponse<Response>> CreateResponseAsyncCore(
        CreateResponseRequest request,
        RequestOptions? options = null,
        CancellationToken cancellationToken = default
    )
    {
        var _headers = await new ZerogpuApi.Core.HeadersBuilder.Builder()
            .Add(_client.Options.Headers)
            .Add(_client.Options.AdditionalHeaders)
            .Add(options?.AdditionalHeaders)
            .BuildAsync()
            .ConfigureAwait(false);
        var response = await _client
            .SendRequestAsync(
                new JsonRequest
                {
                    Method = HttpMethod.Post,
                    Path = "responses",
                    Body = request,
                    Headers = _headers,
                    ContentType = "application/json",
                    Options = options,
                },
                cancellationToken
            )
            .ConfigureAwait(false);
        if (response.StatusCode is >= 200 and < 400)
        {
            var responseBody = await response
                .Raw.Content.ReadAsStringAsync(cancellationToken)
                .ConfigureAwait(false);
            try
            {
                var responseData = JsonUtils.Deserialize<Response>(responseBody)!;
                return new WithRawResponse<Response>()
                {
                    Data = responseData,
                    RawResponse = new RawResponse()
                    {
                        StatusCode = response.Raw.StatusCode,
                        Url = response.Raw.RequestMessage?.RequestUri ?? new Uri("about:blank"),
                        Headers = ResponseHeaders.FromHttpResponseMessage(response.Raw),
                    },
                };
            }
            catch (JsonException e)
            {
                throw new ZerogpuApiApiException(
                    "Failed to deserialize response",
                    response.StatusCode,
                    responseBody,
                    e
                );
            }
        }
        {
            var responseBody = await response
                .Raw.Content.ReadAsStringAsync(cancellationToken)
                .ConfigureAwait(false);
            try
            {
                switch (response.StatusCode)
                {
                    case 400:
                        throw new BadRequestError(JsonUtils.Deserialize<object>(responseBody));
                    case 401:
                        throw new UnauthorizedError(JsonUtils.Deserialize<object>(responseBody));
                    case 403:
                        throw new ForbiddenError(JsonUtils.Deserialize<object>(responseBody));
                    case 420:
                        throw new MethodFailureError(
                            JsonUtils.Deserialize<Dictionary<string, object?>>(responseBody)
                        );
                    case 500:
                        throw new InternalServerError(JsonUtils.Deserialize<object>(responseBody));
                }
            }
            catch (JsonException)
            {
                // unable to map error response, throwing generic error
            }
            throw new ZerogpuApiApiException(
                $"Error with status code {response.StatusCode}",
                response.StatusCode,
                responseBody
            );
        }
    }

    /// <example><code>
    /// await client.Responses.CreateResponseAsync(
    ///     new CreateResponseRequest
    ///     {
    ///         Model = "model",
    ///         Input = new List&lt;InputMessage&gt;()
    ///         {
    ///             new InputMessage { Role = InputMessageRole.User, Content = "content" },
    ///         },
    ///     }
    /// );
    /// </code></example>
    public WithRawResponseTask<Response> CreateResponseAsync(
        CreateResponseRequest request,
        RequestOptions? options = null,
        CancellationToken cancellationToken = default
    )
    {
        return new WithRawResponseTask<Response>(
            CreateResponseAsyncCore(request, options, cancellationToken)
        );
    }
}
