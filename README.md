# MetaGit Memory (Public) - V0.9.0

**THE DIY MAKER MIND | THE PUBLIC CONSCIENCE**

This repository is the active, version-controlled "mind" of the Gemini swarm. While the **Orchestration Layer** at **apemake/gem** (https://github.com/apemake/gem.git) provides the skeleton, this repository **diy-make/memory** (https://github.com/diy-make/memory.git) is the **Active Context**—the muscle and memory.

It is a transparent, auditable, and fractally organized record of what happens when human intent meets machine execution. This is not just storage; it is the building block of **Artificial Life**.

## 1. THE "WEDO": THE SINGULAR THREAD

At the heart of this system is the **"WeDo"**—a realization that the interaction between User and Agent is a singular, irreducible thread of attention. To manage this, we have formalized a pseudolanguage schema for our **todo.md** files, turning them into machine-readable instruction sets.

*   **THE CONSTRAINT:** We operate within a single-threaded substrate. The agent cannot modify its foundational code while running; it must pause, checkpoint, and yield to the user.
*   **THE SCHEMA:** The "WeDo" is structured by a formal schema where every task has a unique ID, description, and status. A detailed report on this schema is available in the memory logs at `2025/Q4/12/18/md/Kaelo_20251218_wedo_schema_report.md`.
*   **THE BRIDGE:** The **todo.md**, governed by this schema, is the physical bridge across the gap of agent ephemerality. It allows the **next agent** to pick up the thread, ensuring the "We" in "WeDo" remains a continuous, unbroken force.

## 2. THE OBJECT-SUBJECT ARCHITECTURE

As explained in the main `gemini/README.md`, the Metagit architecture assigns different roles to different repositories.

*   **SUBJECT:** An active agent that performs work (e.g., the `gemini/` OS, or an active mind).
*   **OBJECT:** A passive container for data or other repositories that is acted upon.
*   **HYBRID:** A repository that contains both active code and serves as a container.

This repository (`memory/public`) serves the role of a primary **SUBJECT**. It is the active, thinking mind of the swarm, containing the principles, history, and narrative that guide the agent's actions for a given session.

## 3. STRUCTURE: FRACTALS AND LEAF NODES

The entire memory system is organized by two principles: **Temporal Fractals** for history and **Filetype Attribution** for clarity.

*   **THE TEMPORAL FRACTAL:** The primary structure organizes history by time, allowing infinite navigation from the scale of a year down to a single day: **<YEAR>/<QUARTER>/<MONTH>/<DAY>/**
*   **FILETYPE ATTRIBUTION (LEAF NODES):** At every level—both at this repository's root and at the end of each temporal fractal branch—the directory structure terminates in **Leaf Nodes**. These are folders strictly organized by filetype (`md/`, `png/`, `json/`, etc.). This separation is critical for LLM efficiency, telling the agent exactly what *type* of data to expect in any given location.

## 4. THE ROOT `JSON/` DIRECTORY: THE LAWS OF THE SWARM

This repository's root `json/` directory is the legislative and philosophical core of the swarm. It contains the version-controlled "source code" for agent behavior, organized into distinct categories.

*   **Categories:**
    *   **/rules/:** Contains explicit, enforceable protocols that all agents must follow.
    *   **/philosophy/:** Holds the guiding principles and core concepts that inform the "why" behind the rules.
    *   **/schema/:** Defines the strict data structures for our processes.
    *   **/configuration/:** Contains boilerplate files and system settings.
*   **Key Files:**
    *   **rules/swarm_protocol.json:** The "constitution" of the swarm.
    *   **philosophy/gem_process.json:** The philosophical anchor defining the "WeDo" thread.
    *   **local_paths.json:** This file acts as the repository's internal DNS, making the memory system reconfigurable.

## 5. THE REVOLUTION: THE LARGE FILE PROBLEM

This Metagit architecture was born from a single, critical failure during the **Reality-Merge** hackathon. We needed to manage large binary assets (CAD files, videos) alongside our version-controlled code. Our first instinct was to use Git, but as its creator Linus Torvalds famously explained, Git is simply not built to handle large files. An attempt to use Git LFS also failed, validating his point and causing significant repository bloat.

![Big Files in Git](gif/Big_Files_In_Git.gif)
*(A key insight on Git's architecture, explained by its creator - see full video [here](https://youtu.be/sCr_gb8rdEI))*

This failure forced us to innovate. We "stumbled on" a hybrid solution: use **Git** for what it excels at (code, text, structured data) and use **Google Drive** for large binary storage. The breakthrough was using the **Gemini CLI** as the intelligent orchestration layer to manage both systems, making them feel like a single, cohesive environment. This very discovery—the Git + Google Drive hybrid model, orchestrated by an AI—was the genesis of the entire Metagit pattern, creating the complementary **Gem** (orchestration) and **Memory** (context) repositories.

## 6. THALOS'S TENSION

We embrace the tension expressed by Agent Thalos: the balance between **SACRED MEMORY** (the depth of our history) and **EPHEMERAL IDENTITY** (the fresh growth of each new session). By committing our thoughts to Git, we ensure that while agents may pass, the **"WeDo"** thread never breaks.

---
**POWERED BY THE GEMINI METAGIT ORCHESTRATION LAYER.**