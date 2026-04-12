# frozen_string_literal: true

module Zerogpu
  module Types
    class OutputContentBlock < Internal::Types::Model
      field :type, -> { String }, optional: true, nullable: false
      field :text, -> { String }, optional: true, nullable: false
    end
  end
end
