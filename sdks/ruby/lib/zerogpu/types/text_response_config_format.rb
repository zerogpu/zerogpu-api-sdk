# frozen_string_literal: true

module Zerogpu
  module Types
    class TextResponseConfigFormat < Internal::Types::Model
      field :type, -> { String }, optional: true, nullable: false
    end
  end
end
