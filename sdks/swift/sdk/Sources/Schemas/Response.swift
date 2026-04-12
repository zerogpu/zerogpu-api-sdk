import Foundation

public struct Response: Codable, Hashable, Sendable {
    public let id: String
    public let object: String
    /// Unix timestamp when the response was created
    public let created: Int64
    public let model: String
    public let output: [OutputMessage]
    public let usage: TokenUsage?
    /// Additional properties that are not explicitly defined in the schema
    public let additionalProperties: [String: JSONValue]

    public init(
        id: String,
        object: String,
        created: Int64,
        model: String,
        output: [OutputMessage],
        usage: TokenUsage? = nil,
        additionalProperties: [String: JSONValue] = .init()
    ) {
        self.id = id
        self.object = object
        self.created = created
        self.model = model
        self.output = output
        self.usage = usage
        self.additionalProperties = additionalProperties
    }

    public init(from decoder: Decoder) throws {
        let container = try decoder.container(keyedBy: CodingKeys.self)
        self.id = try container.decode(String.self, forKey: .id)
        self.object = try container.decode(String.self, forKey: .object)
        self.created = try container.decode(Int64.self, forKey: .created)
        self.model = try container.decode(String.self, forKey: .model)
        self.output = try container.decode([OutputMessage].self, forKey: .output)
        self.usage = try container.decodeIfPresent(TokenUsage.self, forKey: .usage)
        self.additionalProperties = try decoder.decodeAdditionalProperties(using: CodingKeys.self)
    }

    public func encode(to encoder: Encoder) throws -> Void {
        var container = encoder.container(keyedBy: CodingKeys.self)
        try encoder.encodeAdditionalProperties(self.additionalProperties)
        try container.encode(self.id, forKey: .id)
        try container.encode(self.object, forKey: .object)
        try container.encode(self.created, forKey: .created)
        try container.encode(self.model, forKey: .model)
        try container.encode(self.output, forKey: .output)
        try container.encodeIfPresent(self.usage, forKey: .usage)
    }

    /// Keys for encoding/decoding struct properties.
    enum CodingKeys: String, CodingKey, CaseIterable {
        case id
        case object
        case created
        case model
        case output
        case usage
    }
}