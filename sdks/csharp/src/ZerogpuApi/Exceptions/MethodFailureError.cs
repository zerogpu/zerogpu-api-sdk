namespace ZerogpuApi;

/// <summary>
/// This exception type will be thrown for any non-2XX API responses.
/// </summary>
[Serializable]
public class MethodFailureError(Dictionary<string, object?> body)
    : ZerogpuApiApiException("MethodFailureError", 420, body)
{
    /// <summary>
    /// The body of the response that triggered the exception.
    /// </summary>
    public new Dictionary<string, object?> Body => body;
}
