# frozen_string_literal: true

module Zerogpu
  module Responses
    module Types
      class CreateResponseRequest < Internal::Types::Model
        field :model, -> { String }, optional: false, nullable: false
        field :input, -> { Internal::Types::Array[Zerogpu::Types::InputMessage] }, optional: false, nullable: false
        field :text, -> { Zerogpu::Types::TextResponseConfig }, optional: true, nullable: false
      end
    end
  end
end
