import Foundation

public struct TokenUsage: Codable, Hashable, Sendable {
    public let inputTokens: Int?
    public let outputTokens: Int?
    public let totalTokens: Int?
    /// Additional properties that are not explicitly defined in the schema
    public let additionalProperties: [String: JSONValue]

    public init(
        inputTokens: Int? = nil,
        outputTokens: Int? = nil,
        totalTokens: Int? = nil,
        additionalProperties: [String: JSONValue] = .init()
    ) {
        self.inputTokens = inputTokens
        self.outputTokens = outputTokens
        self.totalTokens = totalTokens
        self.additionalProperties = additionalProperties
    }

    public init(from decoder: Decoder) throws {
        let container = try decoder.container(keyedBy: CodingKeys.self)
        self.inputTokens = try container.decodeIfPresent(Int.self, forKey: .inputTokens)
        self.outputTokens = try container.decodeIfPresent(Int.self, forKey: .outputTokens)
        self.totalTokens = try container.decodeIfPresent(Int.self, forKey: .totalTokens)
        self.additionalProperties = try decoder.decodeAdditionalProperties(using: CodingKeys.self)
    }

    public func encode(to encoder: Encoder) throws -> Void {
        var container = encoder.container(keyedBy: CodingKeys.self)
        try encoder.encodeAdditionalProperties(self.additionalProperties)
        try container.encodeIfPresent(self.inputTokens, forKey: .inputTokens)
        try container.encodeIfPresent(self.outputTokens, forKey: .outputTokens)
        try container.encodeIfPresent(self.totalTokens, forKey: .totalTokens)
    }

    /// Keys for encoding/decoding struct properties.
    enum CodingKeys: String, CodingKey, CaseIterable {
        case inputTokens = "input_tokens"
        case outputTokens = "output_tokens"
        case totalTokens = "total_tokens"
    }
}