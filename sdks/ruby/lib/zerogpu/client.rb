# frozen_string_literal: true

module Zerogpu
  class Client
    # @param base_url [String, nil]
    # @param api_key [String]
    #
    # @return [void]
    def initialize(api_key:, base_url: nil)
      @raw_client = Zerogpu::Internal::Http::RawClient.new(
        base_url: base_url || Zerogpu::Environment::PRODUCTION,
        headers: {
          "X-Fern-Language" => "Ruby",
          "x-api-key" => api_key.to_s
        }
      )
    end

    # @return [Zerogpu::Responses::Client]
    def responses
      @responses ||= Zerogpu::Responses::Client.new(client: @raw_client)
    end
  end
end
