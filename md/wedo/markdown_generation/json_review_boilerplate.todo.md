# WeDo Template: JSON Review & Audit Boilerplate (V2.2 - Watched Automation & Consensus Queue)

## Schema Definition
This boilerplate governs the high-volume, 1-by-1 audit of the Metagit JSON store.

1.  **Entry Presentation:** Show the raw JSON content and its path.
2.  **Watched Automation Protocol:** 
    - The agent assumes "RECOMMENDATION" for all entries.
    - Each entry is processed individually (1-by-1) to avoid JavaScript Heap OOM (Memory Bloom).
    - The agent presents the result "straightup" in the CLI for real-time user monitoring.
    - **Synaptic Feedback:** The agent must wait for user confirmation (explicit or implicit "go ahead") before performing destructive actions (DELETE/MOVE) on sensitive files.
    - **Boomerang Principle:** If the agent encounters a file that violates the schema or is ambiguous, it must report it immediately before proceeding.
3.  **Consensus Queueing (The Heartwood Rule):**
    - **The Queue:** Destructive recommendations (DELETE/MOVE) are not executed immediately. They are added to a **Consensus Queue**.
    - **Presentation:** The queue is presented "straightup" at the end of each audit cycle or upon user request.
    - **Consensus:** Execution only occurs after the user provides explicit **Consensus** (e.g., "APPLY QUEUE").
4.  **Internal Versioning Mandate:** 
    - **Requirement:** Every JSON file in the Heartwood must contain a `"version"` key.
    - **Recommendation:** Default to `"version": "1.0"` if missing.
5.  **Audit & Progress Tracking:** 
    - All decisions are appended to `audit_log.json` immediately.
    - **Metabolic Cycle (The 10-Rule):** Every 10 entries, the agent MUST:
        1. Render the audit log using the provided `.py` companion (e.g., `python3 audit_log.py audit_log.json`).
        2. Perform a Metagit commit of the memory repository to preserve state.
        3. Regenerate the metarepo map using `python3 py/metagit_metarepo_map.py` to ensure structural visibility.
    - `todo.json` is updated every 10 entries to track session velocity.

## Presentation Protocol
- Present "straightup" (no triple-backticks for the report text).
- Display: **Entry N of TOTAL | Path | Recommendation | Decision: PENDING_CONSENSUS (Queued)**.
- For KEEP decisions: **Entry N of TOTAL | Path | Recommendation | Decision: APPLIED (Kept)**.