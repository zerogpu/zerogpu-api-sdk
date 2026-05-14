using ZerogpuApi;

static void LoadDotenv(string path)
{
    if (!File.Exists(path)) return;
    foreach (var line in File.ReadAllLines(path))
    {
        var t = line.Trim();
        if (t.Length == 0 || t.StartsWith('#')) continue;
        var idx = t.IndexOf('=');
        if (idx <= 0) continue;
        var k = t[..idx].Trim();
        var v = t[(idx + 1)..].Trim().Trim('"', '\'');
        if (string.IsNullOrEmpty(Environment.GetEnvironmentVariable(k)))
            Environment.SetEnvironmentVariable(k, v);
    }
}

// Base dir is bin/Debug/net8.0 when using dotnet run
var smokeCsharp = Path.GetFullPath(Path.Combine(AppContext.BaseDirectory, "..", ".."));
LoadDotenv(Path.Combine(smokeCsharp, ".env"));
var workspaceRoot = Path.GetFullPath(Path.Combine(smokeCsharp, "..", "..", ".."));
LoadDotenv(Path.Combine(workspaceRoot, "Benchmark", ".env"));

var apiKey = Environment.GetEnvironmentVariable("ZEROGPU_API_KEY")?.Trim();
var projectId = Environment.GetEnvironmentVariable("ZEROGPU_PROJECT_ID")?.Trim();
var model = Environment.GetEnvironmentVariable("ZEROGPU_MODEL")?.Trim();
if (string.IsNullOrEmpty(apiKey) || string.IsNullOrEmpty(projectId))
{
    Console.Error.WriteLine("Set ZEROGPU_API_KEY and ZEROGPU_PROJECT_ID");
    Environment.Exit(1);
}
if (string.IsNullOrEmpty(model))
{
    Console.Error.WriteLine("Set ZEROGPU_MODEL");
    Environment.Exit(1);
}

var prompt = Environment.GetEnvironmentVariable("ZEROGPU_INPUT_TEXT")?.Trim();
if (string.IsNullOrEmpty(prompt))
    prompt = "In one short sentence, what is a habit tracker?";

var client = new ZerogpuApiClient(projectId, apiKey);
var wrapped = await client.Responses.CreateResponseAsync(
    new CreateResponseRequest
    {
        Model = model,
        Input = new List<InputMessage>
        {
            new() { Role = InputMessageRole.User, Content = prompt },
        },
        Text = new TextResponseConfig { Format = new TextResponseConfigFormat { Type = "text" } },
    }
);

var res = wrapped.Data;
Console.WriteLine($"id: {res.Id}");
Console.WriteLine($"model: {res.Model}");
Console.WriteLine($"usage: {res.Usage}");
