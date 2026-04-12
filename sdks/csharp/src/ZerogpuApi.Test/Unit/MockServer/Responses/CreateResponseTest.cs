using NUnit.Framework;
using ZerogpuApi;
using ZerogpuApi.Test.Unit.MockServer;
using ZerogpuApi.Test.Utils;

namespace ZerogpuApi.Test.Unit.MockServer.Responses;

[TestFixture]
[Parallelizable(ParallelScope.Self)]
public class CreateResponseTest : BaseMockServerTest
{
    [NUnit.Framework.Test]
    public async Task MockServerTest()
    {
        const string requestJson = """
            {
              "model": "model",
              "input": [
                {
                  "role": "user",
                  "content": "content"
                }
              ]
            }
            """;

        const string mockResponse = """
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
            """;

        Server
            .Given(
                WireMock
                    .RequestBuilders.Request.Create()
                    .WithPath("/responses")
                    .WithHeader("Content-Type", "application/json")
                    .UsingPost()
                    .WithBodyAsJson(requestJson)
            )
            .RespondWith(
                WireMock
                    .ResponseBuilders.Response.Create()
                    .WithStatusCode(200)
                    .WithBody(mockResponse)
            );

        var response = await Client.Responses.CreateResponseAsync(
            new CreateResponseRequest
            {
                Model = "model",
                Input = new List<InputMessage>()
                {
                    new InputMessage { Role = InputMessageRole.User, Content = "content" },
                },
            }
        );
        JsonAssert.AreEqual(response, mockResponse);
    }
}
