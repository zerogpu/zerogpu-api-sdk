# frozen_string_literal: true

module Zerogpu
  module Types
    class Response < Internal::Types::Model
      field :id, -> { String }, optional: false, nullable: false
      field :object, -> { String }, optional: false, nullable: false
      field :created, -> { Integer }, optional: false, nullable: false
      field :model, -> { String }, optional: false, nullable: false
      field :output, -> { Internal::Types::Array[Zerogpu::Types::OutputMessage] }, optional: false, nullable: false
      field :usage, -> { Zerogpu::Types::TokenUsage }, optional: true, nullable: false
    end
  end
end
