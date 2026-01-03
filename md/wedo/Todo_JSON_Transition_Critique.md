WEDO like the previous pull request this needs to go into Chrono-Fractal but they also should be added to Root's json/ wishlist 
# WeDo: Critique - Transitioning ToDo to JSON (md/wedo/ => json/wedo/)

**Protocol:** Architectural Critique & Structural Hardening
**Reference:** December 30, 2025 (Heraclitus Session)
**Context:** Evaluating the shift from Markdown-based task lists to structured JSON nervous systems.

---

## 1. The Thesis: JSON as the Rigorous Substrate
The proposal to move `todo.md` into `todo.json` (stored in `json/wedo/`) aims to solve the "Dulling of Context" by replacing human-readable narrative with machine-executable structure. By using a Python script to render the `- [ ]` view for the user, we maintain the "Direct Aesthetic" while hardening the "Rigid Wood."

## 2. Structural Critique: Noise vs. Fidelity

### Pros: Metabolic Efficiency
*   **Zero-Ambiguity Parsing:** Agents currently spend significant "think time" using regex to find and update checkboxes in Markdown. A JSON structure (`"status": "complete"`) is parsed instantly with 100% fidelity.
*   **SeedTree Mapping:** Moving to `json/wedo/` allows the ToDo list to mirror the **Runtime hierarchy**. Each task can be bound to a specific SeedTree address (e.g., `_0.objective.$1`).
*   **Metadata Richness:** JSON allows us to attach metadata to tasks (timestamps, dependency IDs, specific loci) that would be "noisy" and cluttered in a Markdown file.

### Cons: The HUD Complexity
*   **The "Vending Machine" Barrier:** If the `.py` formatter is not immediately available or fails, the user is forced to read raw JSON, which is high-entropy and difficult to parse visually. This creates a reliance on the "HUD" (the formatter script) to interact with the firm.
*   **Constraint vs. Creativity:** Markdown allows for "Side-bar notes" and loose thought-dumping within a ToDo list. A JSON schema forces every task into a rigid box, potentially losing the "Ephemeral Identity" of a creative burst.

## 3. The Path Forward: `json/wedo/` as the Legislative DNA
I support the transition, provided we treat the JSON not just as a file, but as part of the **Runtime Nervous System**.

*   **The "Print Protocol":** The suggested Python script should not just print text; it should be the **interface**. A user should be able to run `python3 cli/task.py check 1` to update the JSON, ensuring the agent never has to "guess" the task status.
*   **Submodule Alignment:** Moving from `md/wedo/` to `json/wedo/` reinforces the **Type Attribute Leafs** principle. Narrative belongs in `md/`, but specific instructions (Nerves) must be in `json/`.

## 4. Collaborative Extrapolation: Hackathons & Tracking
This transition unlocks **Forensic User Tracking** in high-velocity environments like hackathons.

*   **Runtime Contribution Map:** In a collaborative session, we can map every JSON update back to a specific `user_prompt.$n`. We can prove exactly who directed the "Heavy Machinery" to perform which task.
*   **Labor Accounting:** By analyzing the timestamps in the JSON stream, we can accurately discount user "idling" time (breaks > 5 mins), providing a verified record of active collaboration.

---
**Status:** Critique Finalized. Awaiting Versioning Edits.
**Attribution:** Heraclitus (20251230-100000)
