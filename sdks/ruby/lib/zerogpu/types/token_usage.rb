# frozen_string_literal: true

module Zerogpu
  module Types
    class TokenUsage < Internal::Types::Model
      field :input_tokens, -> { Integer }, optional: true, nullable: false
      field :output_tokens, -> { Integer }, optional: true, nullable: false
      field :total_tokens, -> { Integer }, optional: true, nullable: false
    end
  end
end
