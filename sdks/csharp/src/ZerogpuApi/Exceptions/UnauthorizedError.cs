namespace ZerogpuApi;

/// <summary>
/// This exception type will be thrown for any non-2XX API responses.
/// </summary>
[Serializable]
public class UnauthorizedError(object body)
    : ZerogpuApiApiException("UnauthorizedError", 401, body);
