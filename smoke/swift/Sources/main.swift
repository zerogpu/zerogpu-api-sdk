import Api
import Foundation

private func parseDotenv(_ path: String) -> [String: String] {
    var out: [String: String] = [:]
    guard let data = try? String(contentsOfFile: path) else { return out }
    for line in data.split(separator: "\n", omittingEmptySubsequences: false) {
        let t = String(line).trimmingCharacters(in: .whitespaces)
        if t.isEmpty || t.hasPrefix("#") { continue }
        guard let eq = t.firstIndex(of: "=") else { continue }
        let k = String(t[..<eq]).trimmingCharacters(in: .whitespaces)
        var v = String(t[t.index(after: eq)...]).trimmingCharacters(in: .whitespaces)
        if v.count >= 2 {
            if (v.hasPrefix("\"") && v.hasSuffix("\"")) || (v.hasPrefix("'") && v.hasSuffix("'")) {
                v.removeFirst()
                v.removeLast()
            }
        }
        if !k.isEmpty { out[k] = v }
    }
    return out
}

private func envValue(_ key: String, files: [String]) -> String {
    var base = ProcessInfo.processInfo.environment
    for f in files {
        for (k, v) in parseDotenv(f) {
            if base[k]?.isEmpty != false {
                base[k] = v
            }
        }
    }
    return (base[key] ?? "").trimmingCharacters(in: .whitespaces)
}

@main
struct ZerogpuSdkSmoke {
    static func main() async throws {
        let cwd = FileManager.default.currentDirectoryPath
        let workspace = URL(fileURLWithPath: cwd)
            .deletingLastPathComponent()
            .deletingLastPathComponent()
            .deletingLastPathComponent()
        let dotenvFiles = [
            URL(fileURLWithPath: cwd).appendingPathComponent(".env").path,
            workspace.appendingPathComponent("Benchmark/.env").path,
        ]

        let key = envValue("ZEROGPU_API_KEY", files: dotenvFiles)
        let pid = envValue("ZEROGPU_PROJECT_ID", files: dotenvFiles)
        let model = envValue("ZEROGPU_MODEL", files: dotenvFiles)
        if key.isEmpty || pid.isEmpty {
            fputs("Set ZEROGPU_API_KEY and ZEROGPU_PROJECT_ID\n", stderr)
            exit(1)
        }
        if model.isEmpty {
            fputs("Set ZEROGPU_MODEL\n", stderr)
            exit(1)
        }

        var prompt = envValue("ZEROGPU_INPUT_TEXT", files: dotenvFiles)
        if prompt.isEmpty {
            prompt = "In one short sentence, what is a habit tracker?"
        }

        let client = ApiClient(apiKey: key, projectId: pid)
        let req = Requests.CreateResponseRequest(
            model: model,
            input: [InputMessage(role: .user, content: prompt)],
            text: TextResponseConfig(format: TextResponseConfigFormat(type: "text"))
        )
        let res = try await client.responses.createResponse(request: req)
        print("id:", res.id)
        print("model:", res.model)
        print("usage:", String(describing: res.usage))
    }
}
