# frozen_string_literal: true

module Zerogpu
  module Types
    class TextResponseConfig < Internal::Types::Model
      field :format, -> { Zerogpu::Types::TextResponseConfigFormat }, optional: true, nullable: false
    end
  end
end
