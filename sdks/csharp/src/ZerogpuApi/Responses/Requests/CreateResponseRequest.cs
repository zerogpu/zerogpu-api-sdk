using global::System.Text.Json.Serialization;
using ZerogpuApi.Core;

namespace ZerogpuApi;

[Serializable]
public record CreateResponseRequest
{
    /// <summary>
    /// Model identifier from the ZeroGPU dashboard (e.g. summarization or IAB classify).
    /// </summary>
    [JsonPropertyName("model")]
    public required string Model { get; set; }

    [JsonPropertyName("input")]
    public IEnumerable<InputMessage> Input { get; set; } = new List<InputMessage>();

    [JsonPropertyName("text")]
    public TextResponseConfig? Text { get; set; }

    /// <inheritdoc />
    public override string ToString()
    {
        return JsonUtils.Serialize(this);
    }
}
