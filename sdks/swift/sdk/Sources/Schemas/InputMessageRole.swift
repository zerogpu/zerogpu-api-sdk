import Foundation

/// Message author role
public enum InputMessageRole: String, Codable, Hashable, CaseIterable, Sendable {
    case user
    case system
}