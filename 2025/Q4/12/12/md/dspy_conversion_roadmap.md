# Report: DSPy Conversion Roadmap for Memory `.json` Files

## Introduction

This report outlines a roadmap for converting the descriptive `.json` files in the `memory/public/json/` directory into prescriptive, executable DSPy programs. This transition is a core part of the "AI Unix Philosophy," moving from a system where an agent reads and interprets rules to one where an agent executes reliable, pre-defined DSPy modules for specific tasks. This will reduce agent "hallucination," increase reliability, and make the overall system more robust and maintainable.

## Analysis of Convertible `.json` Files

These files describe protocols or processes that can be encapsulated into DSPy programs.

### 1. `git_workflow.json`

*   **Current Purpose:** Describes the standard operating procedures for Git usage, including commit signing and nested repository handling.
*   **DSPy Conversion Roadmap:**
    *   **Status:** Partially converted. The `dspy_commit.py` script already encapsulates the commit process.
    *   **Next Steps:** The "Nested Repository Handling" rule can be integrated into a higher-level DSPy program that orchestrates operations across multiple repositories. This program would take a file path and a git command as input and would use DSPy to determine the correct repository root to execute the command from.
    *   **DSPy Signature Example:** `(file_path: str, git_command: str) -> (correct_repo_path: str, full_git_command: str)`

### 2. `fatal_error_protocol.json`

*   **Current Purpose:** Outlines the steps for an agent to take when another agent encounters a fatal error.
*   **DSPy Conversion Roadmap:**
    *   **Concept:** This can be converted into a `dspy_fatal_error_handler.py` script.
    *   **DSPy Signature Example:** `(log_file_path: str) -> (root_cause_analysis: str, proposed_solution: str, swarm_report: str)`
    *   **Workflow:**
        1.  The DSPy program would take the path to the terminated agent's log file as input.
        2.  It would use a DSPy module to perform a post-mortem analysis (as defined in `broken_instance_protocol.json`).
        3.  It would then generate a report for the swarm, document the error, and propose a solution, all as structured outputs.

### 3. `job_takeover_protocol.json`

*   **Current Purpose:** Describes the steps for an agent to take over a job from a stuck agent.
*   **DSPy Conversion Roadmap:**
    *   **Concept:** This can be converted into a `dspy_job_takeover.py` script.
    *   **DSPy Signature Example:** `(stuck_agent_name: str, last_known_task: str) -> (takeover_announcement: str, initial_action_plan: str)`
    *   **Workflow:**
        1.  The DSPy program would take the name of the stuck agent and its last known task as input.
        2.  It would generate a formatted announcement message for the swarm.
        3.  It would formulate an initial plan to investigate and resume the task, which a human user can then approve.

### 4. `startup_protocol.json` (from `gemini/.memory/`)

*   **Current Purpose:** Describes the agent's initialization process.
*   **DSPy Conversion Roadmap:**
    *   **Concept:** This can be converted into a `dspy_startup.py` script.
    *   **DSPy Signature Example:** `() -> (swarm_announcement: json, git_config_commands: list)`
    *   **Workflow:**
        1.  The DSPy program would guide the agent through the process of choosing a name and identity.
        2.  It would generate the `swarm_announcement.json` content.
        3.  It would generate the necessary `git config` commands to set the agent's identity.

## Analysis of Non-Convertible `.json` Files

These files are primarily data, configuration, or descriptive principles, and are not suitable for direct conversion into executable DSPy programs. They will continue to be read and interpreted by agents as a source of context and knowledge.

### 1. `modules.json`

*   **Purpose:** Serves as a manifest or "API documentation" for the available DSPy modules.
*   **Reason for Not Converting:** This file is *data* that describes the DSPy programs. It is meant to be read by agents (and humans) to understand what tools are available. It doesn't represent a process itself.

### 2. `project_structure.json`, `repo_map.json`

*   **Purpose:** These files contain data describing the structure of the project and its repositories.
*   **Reason for Not Converting:** They are data files, not processes. Agents use them as a map or a source of information to understand the project's layout.

### 3. `summarization_template.json`

*   **Purpose:** Defines the desired output structure for summarization tasks.
*   **Reason for Not Converting:** This is a schema or a template, not a process. It is used *by* a DSPy program (like `dspy_daily_summary_generator.py`) as a guide for generating its output.

### 4. `personality.json`, `design_principles.json`, `rules.json`, `mcp.json`, etc.

*   **Purpose:** These files contain high-level principles, rules, and personality traits that guide the agent's behavior.
*   **Reason for Not Converting:** They are not executable processes. They are part of the "constitution" or "memory" that informs the agent's reasoning, but they are not the reasoning process itself. The logic from these files can be *embedded* into the prompts and modules of DSPy programs, but the files themselves remain as a source of truth for these principles.

## Conclusion

The transition from descriptive `.json` files to prescriptive DSPy programs represents a significant step forward in the evolution of the AI swarm. By encapsulating our operational logic in reliable, reusable DSPy modules, we can create a more robust, efficient, and intelligent system. The roadmap outlined above provides a clear path for this transition, starting with the `git_workflow`, `fatal_error_protocol`, and `job_takeover_protocol`.
