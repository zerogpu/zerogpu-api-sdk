using global::System.Text.Json;
using global::System.Text.Json.Serialization;
using ZerogpuApi.Core;

namespace ZerogpuApi;

[Serializable]
public record InputMessage : IJsonOnDeserialized
{
    [JsonExtensionData]
    private readonly IDictionary<string, JsonElement> _extensionData =
        new Dictionary<string, JsonElement>();

    /// <summary>
    /// Message author role
    /// </summary>
    [JsonPropertyName("role")]
    public required InputMessageRole Role { get; set; }

    /// <summary>
    /// Message text
    /// </summary>
    [JsonPropertyName("content")]
    public required string Content { get; set; }

    [JsonIgnore]
    public ReadOnlyAdditionalProperties AdditionalProperties { get; private set; } = new();

    void IJsonOnDeserialized.OnDeserialized() =>
        AdditionalProperties.CopyFromExtensionData(_extensionData);

    /// <inheritdoc />
    public override string ToString()
    {
        return JsonUtils.Serialize(this);
    }
}
