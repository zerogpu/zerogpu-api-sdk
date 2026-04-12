# Reference
## Responses
<details><summary><code>client.responses.<a href="/Sources/Resources/Responses/ResponsesClient.swift">createResponse</a>(request: Requests.CreateResponseRequest, requestOptions: RequestOptions?) -> Response</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```swift
import Foundation
import Api

private func main() async throws {
    let client = ApiClient(
        apiKey: "<value>",
        projectId: "<x-project-id>"
    )

    _ = try await client.responses.createResponse(request: .init(
        model: "model",
        input: [
            InputMessage(
                role: .user,
                content: "content"
            )
        ]
    ))
}

try await main()
```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request:** `Requests.CreateResponseRequest` 
    
</dd>
</dl>

<dl>
<dd>

**requestOptions:** `RequestOptions?` — Additional options for configuring the request, such as custom headers or timeout settings.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

