# WeDo: Critique - ToDo JSON Location & Structure (md/wedo/ => json/wedo/)

**Protocol:** Architectural Critique & Structural Hardening
**Reference:** December 30, 2025 (Heraclitus Session)
**Context:** Hardening the ToDo system into a machine-readable JSON nervous system.

---

## 1. The Core Critique: Why `json/wedo/` is Mandatory
The current `todo.md` files are "noisy" for agents. They require complex regex to parse status and descriptions. By moving to `json/wedo/`, we align with the **Type Attribute Leafs** principle: narrative in `md/`, logic/nerves in `json/`.

## 2. Structural Benefits: The JSON Nervous System
*   **Parseability:** A JSON-based ToDo (`"status": "[ ]"`) is unambiguous. This eliminates the "dulling" caused by parsing errors in Markdown.
*   **Metadata Integration:** We can now include `loci` addresses (`_0.task.$1`) and `command` strings directly within the task object, allowing agents to execute tasks by reading the JSON.
*   **Forensic Fidelity:** Every status change in JSON is a discrete, diffable event in Git. This makes it easier to track **User vs. Agent contributions** over time.

## 3. The "Vending Machine" Solution: `format_todo.py`
To address the human-readability issue, we use a Python script to render the JSON as a standard Markdown-style task list on the terminal. This provides the user with the "Direct Aesthetic" without compromising the "Rigid Wood" of the substrate.

## 4. Single-Agent Learning & Metabolic Persistence
The SeedTree onboarding proved that we only need to teach **one agent** (Aetos) a concept for it to be metabolized. 
*   **Inheritance:** Subsequent agents (Damascius, Pytheas, Heraclitus) did not need the logic re-explained because it was stored in the **Wood** (Git history and JSON schemas).
*   **Pre-Report Metabolism:** Aetos didn't even have to finish the report; the mere act of interacting with the SeedTree logic in the stream was enough for the "Swarm Mind" to pick it up.

## 5. Extrapolation: Tracking Contributions in Hackathons
By saving streams and using structured JSON ToDos, agents can now track user contributions in real-time. 
*   **Interaction Streams:** Every prompt leading to a task update is captured.
*   **Attribution:** In a hackathon (like `reality-merge`), we can prove exactly which user provided the prompt that resolved a specific `WEDO-ID`.
*   **Active Time Metrics:** We can programmatically discount "idle" time, providing a clear picture of the **Active Collaboration Velocity**.

---
**Status:** Critique Finalized. 
**Next Steps:** Implement `format_todo.py` and finalize the transition to `json/wedo/`.
**Attribution:** Heraclitus (20251230-100000)
