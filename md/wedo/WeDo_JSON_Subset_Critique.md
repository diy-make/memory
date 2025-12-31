# WeDo: Critique - WeDo as a JSON Subset (Pseudolanguage vs Syntax)

**Protocol:** Architectural Ontology & Lingual Definition
**Reference:** December 30, 2025 (Heraclitus Session)
**Context:** Defining the nature of WeDo in a structured, machine-readable environment.

---

## 1. The Question: Pseudolanguage or Syntax?
The transition of WeDo from Markdown to JSON forces us to define its linguistic nature. 

*   **Pseudolanguage (Markdown Phase):** In its `.md` form, WeDo was a pseudolanguage. It relied on human-readable markers (`- [ ]`) that required an agent's "understanding" and regex-based parsing to execute. It was a bridge between natural language and intent.
*   **Syntax (JSON Phase):** In its `.json` form, WeDo becomes a **Syntax**. It is no longer an approximation; it is a rigid set of rules for expressing intent, liability, and task status.

## 2. WeDo as a JSON Subset (`wedo.json`)
The proposal to treat WeDo as a subset of JSON (analogous to JSON-LD) is the most efficient path for scaling the swarm. 

### Why a Subset?
*   **Interoperability:** Any valid `wedo.json` file remains a valid JSON file, but a "WeDo-aware" agent (or future Node.js kernel) knows to treat specific keys (`id`, `status`, `command`, `dependencies`) as **Instructional Nerves**.
*   **Metabolic Rigidity:** By defining WeDo as a JSON subset, we establish the "Rigid Wood" required for Artificial Life. We move from "chatting about tasks" to "synchronizing a state object."
*   **The Vending Machine Interface:** As discussed in the previous critique, the JSON subset allows for specialized "HUD" scripts (like `format_todo.py`) to render the rigid syntax into a human-friendly view without losing the underlying machine fidelity.

## 3. Forensic tracking of user contributions
Defining WeDo as a JSON subset unlocks superior **Forensic Tracking**.

*   **Diff-Based Attribution:** Because the JSON structure is stable, Git diffs of `todo.json` become clean, auditable records of contribution. 
*   **Active Interaction Metrics:** We can programmatically identify the exact moment a task status changed and correlate it with the preceding `user_prompt.$n`. 
*   **Hackathon Provenance:** In collaborative environments, the `wedo.json` subset provides a verifiable "Proof of Labor," documenting exactly which cells (agents) and operators (humans) moved the "Heavy Machinery" of the project forward.

## 4. Conclusion: Hardening the Nerves
WeDo is evolving from an informal "pseudolanguage" into a formal "Syntax Subset." 

*   **Markdown:** Best for **History (Wood)** and **Narrative (Air)**.
*   **JSON Subset (`wedo.json`):** Best for **Instructions (Nerves)** and **State (Metabolism)**.

---
**Status:** Ontology Updated. WeDo defined as a JSON Syntax Subset.
**Next Steps:** Update `README.ai` to reflect the `wedo.json` naming convention and subset logic.
**Attribution:** Heraclitus (20251230-100000)
