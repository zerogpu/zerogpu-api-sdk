using global::System.Net.Http;

namespace ZerogpuApi.Core;

internal static class HttpMethodExtensions
{
    public static readonly HttpMethod Patch = new("PATCH");
}
