import Foundation

public struct OutputMessage: Codable, Hashable, Sendable {
    public let type: String?
    public let role: String?
    public let content: [OutputContentBlock]?
    /// Additional properties that are not explicitly defined in the schema
    public let additionalProperties: [String: JSONValue]

    public init(
        type: String? = nil,
        role: String? = nil,
        content: [OutputContentBlock]? = nil,
        additionalProperties: [String: JSONValue] = .init()
    ) {
        self.type = type
        self.role = role
        self.content = content
        self.additionalProperties = additionalProperties
    }

    public init(from decoder: Decoder) throws {
        let container = try decoder.container(keyedBy: CodingKeys.self)
        self.type = try container.decodeIfPresent(String.self, forKey: .type)
        self.role = try container.decodeIfPresent(String.self, forKey: .role)
        self.content = try container.decodeIfPresent([OutputContentBlock].self, forKey: .content)
        self.additionalProperties = try decoder.decodeAdditionalProperties(using: CodingKeys.self)
    }

    public func encode(to encoder: Encoder) throws -> Void {
        var container = encoder.container(keyedBy: CodingKeys.self)
        try encoder.encodeAdditionalProperties(self.additionalProperties)
        try container.encodeIfPresent(self.type, forKey: .type)
        try container.encodeIfPresent(self.role, forKey: .role)
        try container.encodeIfPresent(self.content, forKey: .content)
    }

    /// Keys for encoding/decoding struct properties.
    enum CodingKeys: String, CodingKey, CaseIterable {
        case type
        case role
        case content
    }
}