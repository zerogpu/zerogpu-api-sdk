import type * as ZerogpuApi from "../index.js";

export interface OutputMessage {
    type?: string | undefined;
    role?: string | undefined;
    content?: ZerogpuApi.OutputContentBlock[] | undefined;
}
