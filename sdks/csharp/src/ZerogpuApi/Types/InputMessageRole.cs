using global::System.Text.Json;
using global::System.Text.Json.Serialization;
using ZerogpuApi.Core;

namespace ZerogpuApi;

[JsonConverter(typeof(InputMessageRole.InputMessageRoleSerializer))]
[Serializable]
public readonly record struct InputMessageRole : IStringEnum
{
    public static readonly InputMessageRole User = new(Values.User);

    public static readonly InputMessageRole System = new(Values.System);

    public InputMessageRole(string value)
    {
        Value = value;
    }

    /// <summary>
    /// The string value of the enum.
    /// </summary>
    public string Value { get; }

    /// <summary>
    /// Create a string enum with the given value.
    /// </summary>
    public static InputMessageRole FromCustom(string value)
    {
        return new InputMessageRole(value);
    }

    public bool Equals(string? other)
    {
        return Value.Equals(other);
    }

    /// <summary>
    /// Returns the string value of the enum.
    /// </summary>
    public override string ToString()
    {
        return Value;
    }

    public static bool operator ==(InputMessageRole value1, string value2) =>
        value1.Value.Equals(value2);

    public static bool operator !=(InputMessageRole value1, string value2) =>
        !value1.Value.Equals(value2);

    public static explicit operator string(InputMessageRole value) => value.Value;

    public static explicit operator InputMessageRole(string value) => new(value);

    internal class InputMessageRoleSerializer : JsonConverter<InputMessageRole>
    {
        public override InputMessageRole Read(
            ref Utf8JsonReader reader,
            Type typeToConvert,
            JsonSerializerOptions options
        )
        {
            var stringValue =
                reader.GetString()
                ?? throw new global::System.Exception(
                    "The JSON value could not be read as a string."
                );
            return new InputMessageRole(stringValue);
        }

        public override void Write(
            Utf8JsonWriter writer,
            InputMessageRole value,
            JsonSerializerOptions options
        )
        {
            writer.WriteStringValue(value.Value);
        }

        public override InputMessageRole ReadAsPropertyName(
            ref Utf8JsonReader reader,
            Type typeToConvert,
            JsonSerializerOptions options
        )
        {
            var stringValue =
                reader.GetString()
                ?? throw new global::System.Exception(
                    "The JSON property name could not be read as a string."
                );
            return new InputMessageRole(stringValue);
        }

        public override void WriteAsPropertyName(
            Utf8JsonWriter writer,
            InputMessageRole value,
            JsonSerializerOptions options
        )
        {
            writer.WritePropertyName(value.Value);
        }
    }

    /// <summary>
    /// Constant strings for enum values
    /// </summary>
    [Serializable]
    public static class Values
    {
        public const string User = "user";

        public const string System = "system";
    }
}
