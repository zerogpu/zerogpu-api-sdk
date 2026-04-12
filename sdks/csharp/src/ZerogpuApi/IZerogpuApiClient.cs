namespace ZerogpuApi;

public partial interface IZerogpuApiClient
{
    public IResponsesClient Responses { get; }
}
