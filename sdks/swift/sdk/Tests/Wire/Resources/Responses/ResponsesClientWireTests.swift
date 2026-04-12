import Foundation
import Testing
import Api

@Suite("ResponsesClient Wire Tests") struct ResponsesClientWireTests {
    @Test func createResponse1() async throws -> Void {
        let stub = HTTPStub()
        stub.setResponse(
            body: Data(
                """
                {
                  "id": "resp_abc123",
                  "object": "response",
                  "created": 1000000,
                  "model": "model",
                  "output": [
                    {
                      "type": "message",
                      "role": "assistant",
                      "content": [
                        {
                          "type": "output_text"
                        }
                      ]
                    }
                  ],
                  "usage": {
                    "input_tokens": 1,
                    "output_tokens": 1,
                    "total_tokens": 1
                  }
                }
                """.utf8
            )
        )
        let client = ApiClient(
            baseURL: "https://api.fern.com",
            apiKey: "<value>",
            projectId: "<x-project-id>",
            urlSession: stub.urlSession
        )
        let expectedResponse = Response(
            id: "resp_abc123",
            object: "response",
            created: 1000000,
            model: "model",
            output: [
                OutputMessage(
                    type: Optional("message"),
                    role: Optional("assistant"),
                    content: Optional([
                        OutputContentBlock(
                            type: Optional("output_text")
                        )
                    ])
                )
            ],
            usage: Optional(TokenUsage(
                inputTokens: Optional(1),
                outputTokens: Optional(1),
                totalTokens: Optional(1)
            ))
        )
        let response = try await client.responses.createResponse(
            request: .init(
                model: "model",
                input: [
                    InputMessage(
                        role: .user,
                        content: "content"
                    )
                ]
            ),
            requestOptions: RequestOptions(additionalHeaders: stub.headers)
        )
        try #require(response == expectedResponse)
    }
}