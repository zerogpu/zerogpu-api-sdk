// swift-tools-version: 5.9
import PackageDescription

let package = Package(
    name: "ZerogpuSdkSmoke",
    platforms: [.macOS(.v12), .iOS(.v15)],
    products: [
        .executable(name: "zerogpu-sdk-smoke", targets: ["ZerogpuSdkSmoke"])
    ],
    dependencies: [
        .package(name: "ZerogpuSwiftSdk", path: "../../sdks/swift/sdk")
    ],
    targets: [
        .executableTarget(
            name: "ZerogpuSdkSmoke",
            dependencies: [
                .product(name: "Api", package: "ZerogpuSwiftSdk")
            ],
            path: "Sources"
        )
    ]
)
