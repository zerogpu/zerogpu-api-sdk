namespace ZerogpuApi;

public partial interface IResponsesClient
{
    WithRawResponseTask<Response> CreateResponseAsync(
        CreateResponseRequest request,
        RequestOptions? options = null,
        CancellationToken cancellationToken = default
    );
}
