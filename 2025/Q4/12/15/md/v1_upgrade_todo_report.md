# Report: V1 Upgrade To-Do List

**1. Objective**

This report documents the "failures" of specific script pipelines, as requested. These scripts are not broken, but they are incompatible with the V1 metagit architecture. Their "failure" is a failure to comply with the new system design. This document outlines the necessary upgrades to make them functional.

**2. Agent Navigation Scripts**

*   **Scripts:** `dspy_startup.py`, `dspy_simple_orchestrator.py`
*   **Analysis:** These scripts are designed to help an uninitiated agent by reading its tasks and configuration from a local `json/` directory. However, they are currently hardcoded to look for this directory in their immediate vicinity.
*   **Required Upgrade:** They need to be refactored to be more flexible. Instead of assuming a local `json/` directory, they should be modified to accept a path to a specific "memory module" (like `repos/diy-make/memory/public/`) as an argument. This will allow them to navigate any agent within any memory context.

**3. Chat Processing & Summarization Pipeline**

*   **Scripts:** `dspy_chat_summarizer.py`, `dspy_daily_summary_generator.py`, `dspy_daily_workflow_orchestrator.py`, `parse_chat_log.py`.
*   **Analysis:** This entire suite of scripts forms a powerful summarization pipeline. However, it is fundamentally broken in the V1 architecture because its inputs and outputs are hardcoded to the now-deprecated `.chat/` directory structure. For example, it looks for input logs in `.chat/unclean/` and saves summaries to `.chat/session_summaries/`.
*   **Required Upgrade:** This pipeline needs a complete architectural refactoring.
    *   **Input:** The orchestrator must be modified to read raw typescript logs from the correct V1 location: the `dynamic/stream/` directory.
    *   **Output:** The scripts must be changed to write their output (cleaned logs, individual reports, daily summaries) to the appropriate date-stamped directories within the active memory module (e.g., `repos/diy-make/memory/public/`).
    *   **Dependencies:** Any reliance on `.memory/` for configuration (like `parsing_config.json`) must be removed and replaced with a V1-compliant method.

These upgrade tasks will be addressed in a future development phase, after we have completed the `dspy_screenshot_organizer.py` task.
