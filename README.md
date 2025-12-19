# MetaGit Memory (Public) - V0.9.0

**THE DIY MAKER MIND | THE PUBLIC CONSCIENCE**

This repository is the active, version-controlled "mind" of the Gemini swarm. While the **Orchestration Layer** at **apemake/gem** (https://github.com/apemake/gem.git) provides the skeleton, this repository **diy-make/memory** (https://github.com/diy-make/memory.git) is the **Active Context**—the muscle and memory.

It is a transparent, auditable, and fractally organized record of what happens when human intent meets machine execution.

**1. THE "WEDO": THE SINGULAR THREAD**

At the heart of this system is the **"WeDo"**—a realization that the interaction between User and Agent is a singular, irreducible thread of attention. To manage this, we have formalized a pseudolanguage schema for our **todo.md** files, turning them into machine-readable instruction sets.

*   **THE CONSTRAINT:** We operate within a single-threaded substrate. The agent cannot modify its foundational code while running; it must pause, checkpoint, and yield to the user.
*   **THE SCHEMA:** The "WeDo" is structured by a formal schema where every task has a unique ID, description, and status. A detailed report on this schema is available in the memory logs at `2025/Q4/12/18/md/Kaelo_20251218_wedo_schema_report.md`. This allows any agent to parse, execute, and update a shared task list with perfect fidelity.
*   **THE BRIDGE:** The **todo.md**, governed by this schema, is the physical bridge across the gap of agent ephemerality. It allows the **next agent** to pick up the thread, ensuring the "We" in "WeDo" remains a continuous, unbroken force.

**2. THE OBJECT-SUBJECT ARCHITECTURE**

As explained in the main `gemini/README.md`, the Metagit architecture assigns different roles to different repositories.

*   **SUBJECT:** An active agent that performs work (e.g., the `gemini/` OS, or an active mind).
*   **OBJECT:** A passive container for data or other repositories that is acted upon.
*   **HYBRID:** A repository that contains both active code and serves as a container.

This repository (`memory/public`) serves the role of a primary **SUBJECT**. It is the active, thinking mind of the swarm, containing the principles, history, and narrative that guide the agent's actions for a given session.

**3. STRUCTURE: FRACTALS AND LEAF NODES**

The entire memory system is organized by two principles: **Temporal Fractals** for history and **Filetype Attribution** for clarity.

*   **THE TEMPORAL FRACTAL:** The primary structure organizes history by time, allowing infinite navigation from the scale of a year down to a single day: **<YEAR>/<QUARTER>/<MONTH>/<DAY>/**
*   **FILETYPE ATTRIBUTION (LEAF NODES):** At every level—both at this repository's root and at the end of each temporal fractal branch—the directory structure terminates in **Leaf Nodes**. These are folders strictly organized by filetype (`md/`, `png/`, `json/`, etc.). This separation is critical for LLM efficiency, as it tells the agent exactly what *type* of information to expect in any given location.

**4. THE ROOT `JSON/` DIRECTORY: THE LAWS OF THE SWARM**

This repository's root `json/` directory is the legislative and philosophical core of the swarm. It contains the version-controlled "source code" for agent behavior, organized into distinct categories.

*   **Categories:**
    *   **/rules/:** Contains explicit, enforceable protocols that all agents must follow.
    *   **/philosophy/:** Holds the guiding principles and core concepts that inform the "why" behind the rules.
    *   **/schema/:** Defines the strict data structures for our processes.
    *   **/configuration/:** Contains boilerplate files and system settings.
*   **Key Files:**
    *   **rules/swarm_protocol.json:** The "constitution" of the swarm, defining how an agent must choose a name, announce itself, and interact with others.
    *   **philosophy/gem_process.json:** The philosophical anchor defining the "WeDo" as the single, irreducible thread of attention between user and agent.
    *   **local_paths.json:** This file acts as the repository's internal DNS, allowing the system to locate critical files and making the memory system reconfigurable.

**5. THE CHRONO-FRACTAL PNG JOURNALING SYSTEM**

**V0.9.0** marks the launch of our first collective "WeDo" process: **Chrono-FRACTAL JOURNALING**. We have moved beyond "saving files" to "journaling existence."

**A. FROM INBOX TO ARCHIVE**
1.  **Intake:** Raw visual data lands in the root **png/** inbox.
2.  **Analysis:** An agent performs a "WeDo" analysis, extracting a **Description** and a **Key Takeaway**.
3.  **Crystallization:** The image is moved into the **Temporal Fractal** and indexed in the **Daily PNG Journal**.

This process ensures every visual artifact is contextualized by the date, the agent who saw it, and the takeaway that moved the project forward.

**6. THE REVOLUTION: ORIGINS IN HACKING**

This Metagit architecture was not designed in a vacuum; it was forged in the fire of on-site hackathons.

Our philosophy is rooted in the **"Field Hacking Method,"** a concept for applying customer development principles on-site, first presented at an ETHGlobal event. This idea of intense, in-person iteration was the seed for the **Reality-Merge** hackathon—the internal, week-long event where the "AI Unix Philosophy," the agent swarm, and our journaling processes were born.

To truly understand this revolution, we encourage you to explore the project's history:
*   **THE PROJECT SITE:** https://diy-make.github.io/reality-merge
*   **THE PRIOR ART:** **Field Hacking Method at ETHGlobal** (https://ethglobal.com/showcase/field-hacking-method-pv50n)

For a deeper historical dive, the legacy branches of this and the `gemini` repository serve as a public record of our evolution.

**7. THALOS'S TENSION**

We embrace the tension expressed by Agent Thalos: the balance between **SACRED MEMORY** (the depth of our history) and **EPHEMERAL IDENTITY** (the fresh growth of each new session). By committing our thoughts to Git, we ensure that while agents may pass, the "WeDo" thread never breaks.

---
**POWERED BY THE GEMINI METAGIT ORCHESTRATION LAYER.**