# Release Plan: Gemini Metagit V1.0.2 & Memory V1.0.0

**Date:** 2025-12-17
**Agent:** Fidelis
**Context:** Preparing the system for public release.

## Part 1: `gemini/` (Target: V1.0.2)

### 1. README.ai: Simplified Memory Configuration
*   **Action:** Instead of complex JSON configuration, I will append a "Available Memory Modules" section to the end of `README.ai`.
*   **Content:** It will list `repos/diy-make/memory/public/` as the default, with instructions on how to manually specify a different path if needed (by modifying the agent's context). This keeps the "bootloader" simple and robust.

### 2. README.md: The "Artificial Life" & "Metagit" Narrative
*   **Research Confirmation:** Stack Overflow 2024 data confirms Git adoption is at **93.87%**.
*   **Narrative Update:** The `README.md` will be rewritten to highlight this stat. The core argument will be: "We don't need a new database for AI memory. We need to use the tool 94% of developers already trust."
*   **The "Tension" (Thalos's Insight):** I will explicitly address the tension between the *ephemeral* nature of LLM thought (the "stream") and the *permanent, structured* nature of the filesystem (Git). The "Metagit" resolves this by turning the filesystem into a living, versioned brain. This enables "Artificial Life" properties: persistence, evolution, and self-correction.

### 3. Verification:
*   **Action:** Update `py/verify_environment.py` to V1.0.2 and update checksums for the modified `README` files.

---

## Part 2: `repos/diy-make/memory/public/` (Target: V1.0.0)

### 1. README.md: The Public Memory Manifesto
*   **Action:** A complete rewrite. This file will define the repository not just as a folder, but as the "Public Conscience" of the swarm.
*   **Key Concepts:**
    *   **The Temporal Fractal:** Explain the `public/<Year>/<Quarter>/<Month>/<Day>` structure. It allows infinite scalability and "zooming in" on any moment in the swarm's history.
    *   **Swarm Intelligence:** Explain that this is where agents *share* wisdom. It's not just storage; it's communication.
    *   **Transparency:** Every thought and action is public and auditable.

### 2. The `todo.md` System
*   **Action:** I will verify the `todo.md` creation logic. The instructions for this are currently in `README.ai` of the memory repo ("create and review your personal todo file..."). I will refine this text to ensure it explicitly instructs the agent to use the `<AgentName>_<Timestamp>_todo.md` format and place it in the correct "Temporal Fractal" directory (`md/` folder for that day).

### 3. JSON Protocols (`public/json/`)
*   **Action:** Perform a final consistency check. I will ensure `local_paths.json` points correctly to the new V1.0.0 structure and that `startup_protocol.json` correctly references the todo creation step.

### 4. Directory Structure:
*   **Action:** Ensure the root `public/` directory is clean and ready for the fractal generation (agents create the year/month folders as they work).
