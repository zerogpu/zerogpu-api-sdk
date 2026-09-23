export const ZerogpuApiEnvironment = {
    Production: "https://api.zerogpu.ai/v1",
} as const;

export type ZerogpuApiEnvironment = typeof ZerogpuApiEnvironment.Production;
