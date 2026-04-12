import Foundation

extension Requests {
    public struct CreateResponseRequest: Codable, Hashable, Sendable {
        /// Model identifier from the ZeroGPU dashboard (e.g. summarization or IAB classify).
        public let model: String
        public let input: [InputMessage]
        public let text: TextResponseConfig?
        /// Additional properties that are not explicitly defined in the schema
        public let additionalProperties: [String: JSONValue]

        public init(
            model: String,
            input: [InputMessage],
            text: TextResponseConfig? = nil,
            additionalProperties: [String: JSONValue] = .init()
        ) {
            self.model = model
            self.input = input
            self.text = text
            self.additionalProperties = additionalProperties
        }

        public init(from decoder: Decoder) throws {
            let container = try decoder.container(keyedBy: CodingKeys.self)
            self.model = try container.decode(String.self, forKey: .model)
            self.input = try container.decode([InputMessage].self, forKey: .input)
            self.text = try container.decodeIfPresent(TextResponseConfig.self, forKey: .text)
            self.additionalProperties = try decoder.decodeAdditionalProperties(using: CodingKeys.self)
        }

        public func encode(to encoder: Encoder) throws -> Void {
            var container = encoder.container(keyedBy: CodingKeys.self)
            try encoder.encodeAdditionalProperties(self.additionalProperties)
            try container.encode(self.model, forKey: .model)
            try container.encode(self.input, forKey: .input)
            try container.encodeIfPresent(self.text, forKey: .text)
        }

        /// Keys for encoding/decoding struct properties.
        enum CodingKeys: String, CodingKey, CaseIterable {
            case model
            case input
            case text
        }
    }
}