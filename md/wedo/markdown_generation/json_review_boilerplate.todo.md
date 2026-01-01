# WeDo Template: JSON Review & Audit Boilerplate (V2.0 - Watched Automation)

## Schema Definition
This boilerplate governs the high-volume, 1-by-1 audit of the Metagit JSON store.

1.  **Entry Presentation:** Show the raw JSON content and its path.
2.  **Watched Automation Protocol:** 
    - The agent assumes "RECOMMENDATION" for all entries.
    - Each entry is processed individually (1-by-1) to avoid JavaScript Heap OOM (Memory Bloom).
    - The agent presents the result "straightup" in the CLI for real-time user monitoring.
3.  **Internal Versioning Mandate:** 
    - **Requirement:** Every JSON file in the Heartwood must contain a `"version"` key.
    - **Recommendation:** Default to `"version": "1.0"` if missing.
4.  **Chrono Context:** 
    - Temporal location is defined by the chrono-fractal filesystem (`YYYY/QN/MM/DD/json/`).
5.  **Audit & Progress Tracking:** 
    - All decisions are appended to `audit_log.json` immediately.
    - `todo.json` is updated every 10 entries to track session velocity.
    - Metagit commits are performed periodically to preserve state.

## Presentation Protocol
- Present "straightup" (no triple-backticks for the report text).
- Display: **Entry N of TOTAL | Path | Recommendation | Decision: RECOMMENDATION (Applied)**.