import Foundation

public final class ResponsesClient: Sendable {
    private let httpClient: HTTPClient

    init(config: ClientConfig) {
        self.httpClient = HTTPClient(config: config)
    }

    public func createResponse(request: Requests.CreateResponseRequest, requestOptions: RequestOptions? = nil) async throws -> Response {
        return try await httpClient.performRequest(
            method: .post,
            path: "/responses",
            body: request,
            requestOptions: requestOptions,
            responseType: Response.self
        )
    }
}