# frozen_string_literal: true

# Live smoke: one POST /v1/responses via Fern-generated Ruby SDK.
# Requires Ruby >= 3.3 (see sdks/ruby/zerogpu.gemspec).

require "bundler/setup"
require "zerogpu"

def load_dotenv_file(path)
  return unless File.file?(path)

  File.foreach(path) do |line|
    line = line.strip
    next if line.empty? || line.start_with?("#")

    k, _, v = line.partition("=")
    k = k.strip
    v = v.strip.sub(/\A['"]/, "").sub(/['"]\z/, "")
    ENV[k] = v unless ENV[k] && !ENV[k].empty?
  end
end

root = File.expand_path("../..", __dir__)
load_dotenv_file(File.join(__dir__, ".env"))
load_dotenv_file(File.expand_path("../Benchmark/.env", root))

api_key = ENV.fetch("ZEROGPU_API_KEY", "").strip
project_id = ENV.fetch("ZEROGPU_PROJECT_ID", "").strip
model = ENV.fetch("ZEROGPU_MODEL", "").strip
if api_key.empty? || project_id.empty?
  warn "Set ZEROGPU_API_KEY and ZEROGPU_PROJECT_ID"
  exit 1
end
if model.empty?
  warn "Set ZEROGPU_MODEL"
  exit 1
end

prompt = ENV.fetch("ZEROGPU_INPUT_TEXT", "").strip
prompt = "In one short sentence, what is a habit tracker?" if prompt.empty?

client = Zerogpu::Client.new(api_key: api_key)

res = client.responses.create_response(
  request_options: { additional_headers: { "x-project-id" => project_id } },
  model: model,
  input: [{ role: Zerogpu::Types::InputMessageRole::USER, content: prompt }],
  text: { format: { type: "text" } }
)

puts "id: #{res.id}"
puts "model: #{res.model}"
puts "usage: #{res.usage.inspect}"
