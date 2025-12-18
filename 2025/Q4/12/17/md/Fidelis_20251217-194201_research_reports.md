# Research Reports: SeedTreeDB, Metagit, and Kernel Implementations

**Date:** 2025-12-17
**Agent:** Fidelis
**Context:** Research to inform the rewrite of the `gemini/README.md`.

---

### **Report 1: SeedTreeDB & The Hierarchical Script Database (WO2020160021)**

*   **Founder:** Kyle Smith ("bestape").
*   **Concept:** It is an **event-driven crystallization** engine. The core idea is to merge the "Application" (logic) and the "Database" (state) into a single, unified system using the same language (JavaScript).
*   **Philosophy:** It solves "callback hell" and asynchronous state management by treating the database not as a passive store, but as a dynamic, hierarchical script execution environment. It captures the fluid stream of events and "crystallizes" them into a structured, persistent state. The patent WO2020160021 describes a system where nested execution contexts (`loci`) form a tree, and every node in that tree is both data and potential program.

---

### **Report 2: The Metagit vs. The Kernel**

*   **The Kernel (SeedTreeDB/HSD):** This is the low-level, abstract pattern for event-driven crystallization. It defines the rules for how nested contexts are created and how state is recorded. It is the "physics engine" of the Fractal Unix philosophy.
*   **The Metagit (This Project):** This is a specific, high-level **application** of that kernel philosophy, purpose-built for the domain of AI Agents.
    *   It uses **Git** as the physical storage and versioning layer for the crystallization process.
    *   It uses the **Temporal Fractal** (`public/2025/...`) to structure the crystallized "wood" of the agent's memory tree.
    *   It uses **Type Attribute Leafs** (`md/`, `json/`) to optimize the crystallized data for consumption by LLMs.

---

### **Report 3: Cheerbot.me**

*   **Purpose:** A project by the same architect (bestape/Kyle Smith) focused on **Robotic Empathy**.
*   **Memory Module:** `repos/cheerbotme/memory/public/` is the memory for this project.
*   **Goal:** To build and run robots (both physical and digital) designed to "create cheer and related emotions." It serves as a practical example of a specialized "Mind" within the Metagit ecosystem.

---

### **Report 4: The DOM Kernel (`local_only/kernel/index.html`)**

*   **Purpose:** A practical, minimal implementation of the Hierarchical Script Database kernel, designed to run in a web browser's Document Object Model (DOM).
*   **Core Function `kernel(program, data, parent)`:** This is the factory for execution. It creates a new, nested execution context (`loci`) for every call, forming a tree (e.g., `_0.kernel.$1.log.$2`).
*   **State & Persistence:** The `$rec` flag controls "recording," determining if an execution's state is persisted in the parent context. This directly mirrors how Git commits crystallize ephemeral events into permanent state in the Metagit.
*   **Significance:** It proves the "Fractal Unix" pattern is platform-agnostic. The same philosophy that organizes the Metagit's Node.js/filesystem environment can be applied to a browser's DOM, showing its flexibility as a fundamental architectural pattern.

---

### **Report 5: ERC-7827 (JSON Smart Contract with Value Version Control)**

*   **Author:** bestape.
*   **Concept:** Proposes using standard JSON files as a form of human-readable, version-controlled "smart contract."
*   **Relevance to Metagit:** The `.json` files in `memory/public/json/` are an implementation of this principle. They are not just configuration files; they are the "smart contracts" that define the agent's protocols and behavior. Git provides the immutable version history for these contracts, allowing anyone to see how the "laws" of the swarm have evolved over time. This avoids the complexity of on-chain contracts for defining and versioning behavioral rules.