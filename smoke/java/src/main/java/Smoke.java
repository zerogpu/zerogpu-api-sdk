import java.nio.file.Files;
import java.nio.file.Path;
import java.util.HashMap;
import java.util.Map;
import java.util.Optional;
import resources.responses.requests.CreateResponseRequest;
import types.InputMessage;
import types.InputMessageRole;
import types.TextResponseConfig;
import types.TextResponseConfigFormat;

/** Live smoke: one POST /v1/responses via Fern-generated Java SDK sources. */
public class Smoke {

  private static Map<String, String> loadDotenv(Path path) throws Exception {
    Map<String, String> out = new HashMap<>();
    if (!Files.isRegularFile(path)) {
      return out;
    }
    for (String line : Files.readAllLines(path)) {
      String t = line.trim();
      if (t.isEmpty() || t.startsWith("#")) {
        continue;
      }
      int eq = t.indexOf('=');
      if (eq <= 0) {
        continue;
      }
      String k = t.substring(0, eq).trim();
      String v = t.substring(eq + 1).trim();
      if (v.length() >= 2
          && ((v.startsWith("\"") && v.endsWith("\"")) || (v.startsWith("'") && v.endsWith("'")))) {
        v = v.substring(1, v.length() - 1);
      }
      if (!k.isEmpty()) {
        out.put(k, v);
      }
    }
    return out;
  }

  private static String pick(Map<String, String> dotenv, String key) {
    String v = System.getenv(key);
    if (v != null && !v.trim().isEmpty()) {
      return v.trim();
    }
    return Optional.ofNullable(dotenv.get(key)).orElse("").trim();
  }

  public static void main(String[] args) throws Exception {
    Path smokeJava = Path.of(System.getProperty("user.dir"));
    Path fernSdk = smokeJava.getParent().getParent();
    Path workspace = fernSdk.getParent();

    Map<String, String> dotenv = new HashMap<>();
    dotenv.putAll(loadDotenv(smokeJava.resolve(".env")));
    for (Map.Entry<String, String> e : loadDotenv(workspace.resolve("Benchmark").resolve(".env")).entrySet()) {
      dotenv.putIfAbsent(e.getKey(), e.getValue());
    }

    String apiKey = pick(dotenv, "ZEROGPU_API_KEY");
    String projectId = pick(dotenv, "ZEROGPU_PROJECT_ID");
    String model = pick(dotenv, "ZEROGPU_MODEL");
    if (apiKey.isEmpty() || projectId.isEmpty()) {
      System.err.println("Set ZEROGPU_API_KEY and ZEROGPU_PROJECT_ID");
      System.exit(1);
    }
    if (model.isEmpty()) {
      System.err.println("Set ZEROGPU_MODEL");
      System.exit(1);
    }

    String prompt = pick(dotenv, "ZEROGPU_INPUT_TEXT");
    if (prompt.isEmpty()) {
      prompt = "In one short sentence, what is a habit tracker?";
    }

    ZerogpuApiClient client =
        ZerogpuApiClient.builder().apiKey(apiKey).projectId(projectId).build();

    CreateResponseRequest req =
        CreateResponseRequest.builder()
            .model(model)
            .addInput(
                InputMessage.builder()
                    .role(InputMessageRole.USER)
                    .content(prompt)
                    .build())
            .text(
                TextResponseConfig.builder()
                    .format(TextResponseConfigFormat.builder().type("text").build())
                    .build())
            .build();

    var res = client.responses().createResponse(req);
    System.out.println("id: " + res.getId());
    System.out.println("model: " + res.getModel());
    System.out.println("usage: " + res.getUsage());
  }
}
