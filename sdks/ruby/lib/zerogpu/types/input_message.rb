# frozen_string_literal: true

module Zerogpu
  module Types
    class InputMessage < Internal::Types::Model
      field :role, -> { Zerogpu::Types::InputMessageRole }, optional: false, nullable: false
      field :content, -> { String }, optional: false, nullable: false
    end
  end
end
