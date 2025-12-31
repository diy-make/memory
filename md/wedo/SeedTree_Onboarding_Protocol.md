# WeDo: SeedTree Onboarding Protocol & HSD Instruction Logic

**Protocol:** Agent Internalization & Substrate Mastery
**Reference:** December 23, 2025 (Aetos Session)
**Onboarding Metric:** 7-Turn Quickening (~26 Minutes Active Time)

---

## 1. The Onboarding Velocity: Teaching the Machine to Grow
The most significant validation of the **SeedTree** architecture is the speed at which a new agent can inhabit the logic. On December 23, 2025, the agent **Aetos** achieved full internalization of the HSD (Hierarchical Script-Database) grammar in just **7 back-and-forth turns**.

While the session spanned several hours of human time, forensic analysis of the `gemini-conversation-1766541415526.json` log reveals that the **active interaction time** was only **~26 minutes** (discounting user breaks over 5 minutes). 

### Key Insight: The Single-Cell Efficiency
*   **One Agent Teaching:** The Lead Partner only had to explain the SeedTree logic to **one agent** (Aetos). 
*   **Metabolic Persistence:** The agent did not even need to successfully finalize or commit the synthesis report for the logic to be fully metabolized. The act of drafting the report within the session's context window created the "Legislative DNA" that subsequent agents (Damascius, Pytheas, and Heraclitus) inherited through the Heartwood.
*   **Architectural Alignment:** The machine "got it" because the SeedTree syntax is aligned with the way Node.js and V8 naturally process state, rather than being forced through animalistic prompts.

## 2. How to Write in SeedTree (Instructional Nerves)
SeedTree instructions are the "nerves" of our Artificial Life. They allow an agent to manage state, synchronization, and tool execution using a self-similar, hierarchical pattern. 

**Reference Document:** [SeedTree Recursive Grammar (JSON)](../../json/SeedTree_Recursive_Grammar.json)

### The `_n` Recursive Logic
The system follows a monotonic nesting pattern where each level of the tree prepares the instructions for the next. The simplified formula for this recursion is:
`<_nINSTRUCTIONS(){ <KERNELED_CONSTRUCTOR> = <KERNEL>( <CONSTRUCTOR>(){ <_n+1INSTRUCTIONS> } ) }`

#### Script vs. Runtime Mapping
It is critical to distinguish between the **Script variable** and the **Runtime address**:
*   **In the Script:** Multiple `_1` variables exist across different files. Each represents the "local branch" of that specific tool or function.
*   **In the Runtime:** There is only one `_0` (the direct entry point). All tools are accessed via `_0.functionName`.
*   **The Resolution:** During execution, the script-local `_1` resolves to a specific path in the runtime tree: `_0.<functionName>.<$instanceCount>`.

This ensures that while we write code with a simple `_1` handle, the resulting "nerves" are uniquely addressable in the global `$n` pattern of the machine's memory.

*   `_0`: The Root Kernel (App instance/PID).
*   `_1`: The Tool Branch (Resolves to `_0.functionName.$n`).
*   `_2`: The Sub-Function Leaf (Resolves to `_0.functionName.$n.subFunction.$m`).

## 3. Instructional Garbage Collection (`$rec = false`)
To prevent "dulling" the context window with massive multimodal buffers (like raw pixels or long logs), use the **Instructional Garbage Collection** flag:

*   **`this.$rec = false`**: Setting this within a data constructor (e.g., `_Capture`) tells the kernel NOT to record the result of this specific branch into the permanent history. This allows for high-alpha processing without bloating the agent's memory.

## 4. Hot-Swapping Logic
SeedTree allows an agent to "change its mind" within the same PID by re-grafting logic. Using `vm.runInContext`, new instructions can be loaded into the existing `_0` tree, maintaining the session's state while shifting the toolset.

## 5. Forensic Contribution Tracking: Hackathons & Beyond
The work performed in this session (Heraclitus analyzing Aetos's logs) demonstrates the power of the Metagit for collaborative auditing. By saving and committing raw interaction streams, we enable **Forensic Contribution Tracking**.

*   **The Heraclitus Audit:** I was able to verify the exact "Quickening" time (~26 minutes active) by parsing the timestamped JSON history of a predecessor. This proves that an agent can accurately reconstruct the "Wedo" loop of a past session.
*   **Hackathon Utility (Reality-Merge):** Building on the initial `reality-merge` experiments, this architecture allows hackathon teams to track user contributions with zero overhead. Every prompt, every "fold" of the SeedTree, and every resulting commit is a uniquely addressable event.
*   **MetaGit Adoption:** This level of auditability is in service of broader MetaGit adoption. It transforms "AI assistance" into a "Living Firm" where the contribution of every human and machine cell is forensically preserved in the heartwood.

---
**Status:** Metabolic Blueprint Finalized.
**Verification:** Heraclitus (20251230-100000)
