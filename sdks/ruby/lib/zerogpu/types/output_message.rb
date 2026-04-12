# frozen_string_literal: true

module Zerogpu
  module Types
    class OutputMessage < Internal::Types::Model
      field :type, -> { String }, optional: true, nullable: false
      field :role, -> { String }, optional: true, nullable: false
      field :content, -> { Internal::Types::Array[Zerogpu::Types::OutputContentBlock] }, optional: true, nullable: false
    end
  end
end
