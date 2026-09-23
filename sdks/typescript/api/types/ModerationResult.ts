/**
 * The verdict for one input. Category keys follow OpenAI's names, e.g. `harassment/threatening`.
 */
export interface ModerationResult {
    /** True when the model flagged the input in one or more categories. */
    flagged?: boolean | undefined;
    /** Per-category boolean verdicts. All 13 categories are always present. */
    categories?: Record<string, boolean> | undefined;
    /** Per-category confidence scores in [0, 1]. */
    category_scores?: Record<string, number> | undefined;
    /** Which input modality triggered each category. */
    category_applied_input_types?: Record<string, string[]> | undefined;
    /** Accepts any additional properties */
    [key: string]: any;
}
