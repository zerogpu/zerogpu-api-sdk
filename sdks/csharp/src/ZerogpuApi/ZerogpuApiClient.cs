using ZerogpuApi.Core;

namespace ZerogpuApi;

public partial class ZerogpuApiClient : IZerogpuApiClient
{
    private readonly RawClient _client;

    public ZerogpuApiClient(
        string projectId,
        string? apiKey = null,
        ClientOptions? clientOptions = null
    )
    {
        clientOptions ??= new ClientOptions();
        var platformHeaders = new Headers(
            new Dictionary<string, string>()
            {
                { "X-Fern-Language", "C#" },
                { "X-Fern-SDK-Name", "ZerogpuApi" },
                { "X-Fern-SDK-Version", Version.Current },
            }
        );
        foreach (var header in platformHeaders)
        {
            if (!clientOptions.Headers.ContainsKey(header.Key))
            {
                clientOptions.Headers[header.Key] = header.Value;
            }
        }
        var clientOptionsWithAuth = clientOptions.Clone();
        var authHeaders = new Headers(
            new Dictionary<string, string>()
            {
                { "x-project-id", projectId },
                { "x-api-key", apiKey ?? "" },
            }
        );
        foreach (var header in authHeaders)
        {
            clientOptionsWithAuth.Headers[header.Key] = header.Value;
        }
        _client = new RawClient(clientOptionsWithAuth);
        Responses = new ResponsesClient(_client);
    }

    public IResponsesClient Responses { get; }
}
