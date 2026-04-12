# frozen_string_literal: true

module Zerogpu
  module Internal
    module Types
      module Unknown
        include Zerogpu::Internal::Types::Type

        def coerce(value)
          value
        end
      end
    end
  end
end
