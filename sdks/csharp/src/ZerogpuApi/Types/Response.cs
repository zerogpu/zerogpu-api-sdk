using global::System.Text.Json;
using global::System.Text.Json.Serialization;
using ZerogpuApi.Core;

namespace ZerogpuApi;

[Serializable]
public record Response : IJsonOnDeserialized
{
    [JsonExtensionData]
    private readonly IDictionary<string, JsonElement> _extensionData =
        new Dictionary<string, JsonElement>();

    [JsonPropertyName("id")]
    public required string Id { get; set; }

    [JsonPropertyName("object")]
    public required string Object { get; set; }

    /// <summary>
    /// Unix timestamp when the response was created
    /// </summary>
    [JsonPropertyName("created")]
    public required long Created { get; set; }

    [JsonPropertyName("model")]
    public required string Model { get; set; }

    [JsonPropertyName("output")]
    public IEnumerable<OutputMessage> Output { get; set; } = new List<OutputMessage>();

    [JsonPropertyName("usage")]
    public TokenUsage? Usage { get; set; }

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
