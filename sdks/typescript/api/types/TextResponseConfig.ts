export interface TextResponseConfig {
    format?: TextResponseConfig.Format | undefined;
}

export namespace TextResponseConfig {
    export interface Format {
        /** Response format type (e.g. `text`) */
        type?: string | undefined;
    }
}
