namespace ZerogpuApi;

/// <summary>
/// Base exception class for all exceptions thrown by the SDK.
/// </summary>
public class ZerogpuApiException(string message, Exception? innerException = null)
    : Exception(message, innerException);
