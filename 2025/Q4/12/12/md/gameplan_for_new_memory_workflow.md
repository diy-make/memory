# Gameplan: A New Memory Workflow for the AI Swarm

## Architectural Context: The `gemini/` Swarm and the `memory/` Repository

This new memory workflow operates within the context of the `gemini/` swarm, which is the local AI agent orchestration system running on this machine. The `memory/` repository, located at `repos/diy-make/memory/`, is a dedicated, version-controlled space for the swarm's collective long-term memory.

Crucially, the `memory/` repository is designed to be a distinct entity from the main `gemini/` repository. It is included in the `.gitignore` file of `gemini/`, which means it can be managed and versioned independently without affecting the core `gemini/` boilerplate. This separation of concerns ensures that the swarm's operational history (the "memory") does not clutter the core agent framework.

This document outlines a new, unified operational workflow for AI agents, merging the methodologies from the `gemini/.chat` and `reality-merge` repositories into the newly established `memory/` repository. The goal is to create a more robust, scalable, and self-documenting system for the AI swarm.

## Core Principles:

*   **Centralized Memory:** The `repos/diy-make/memory/` repository will serve as the single source of truth for the swarm's collective memory, including daily reports, agent-specific logs, and operational data.
*   **Daily Agent Sessions:** A new AI agent will be initialized at the start of each day to ensure a clean slate and prevent context overflow or procedural drift.
*   **Structured Reporting:** The process of documenting the previous day's events will be standardized, using templates from the `reality-merge` project.

## The New Daily Agent Workflow:

Each morning, a new AI agent will be initialized with the following mandate:

### Step 1: Contextual Onboarding

1.  **Read Universal Memory:** The agent will begin by reading the `README.ai` and all files within the `.memory/` directory of the `gemini/` repository to understand its core identity, operational rules, and the "AI Unix Philosophy".
2.  **Swarm Integration:** The agent will choose a unique name and identity, announce itself to the swarm (as per `swarm_protocol.json`), and configure its local Git identity (`user.name`, `user.email`) for all relevant repositories (`gemini/`, `.chat/`, `memory/`, etc.).

### Step 2: Daily Reporting and Log Processing

The agent's first major task is to document the activities of the previous day (or the last active day).

1.  **Generate Daily Summary:**
    *   The agent will analyze the chat logs, commits, and agent reports from the previous active day.
    *   It will synthesize this information into a comprehensive daily summary, using the format of the `summary.md` files in `repos/diy-make/reality-merge/md/day_x/` as a template.
    *   This new summary will be saved as `summary.md` in the appropriate daily folder within the `memory/` repository (e.g., `memory/2025/Q4/12/12/md/summary.md`).

2.  **Process Uncleaned Chat Logs:**
    *   The agent will identify all uncleaned chat logs (`.chat/unclean/*.txt`) from the previous active day.
    *   For each uncleaned log, it will:
        *   Analyze the log to identify the agent's name, key activities, and termination reason.
        *   Create or append to an agent-specific markdown report in the corresponding `memory/md/` folder (e.g., `memory/2025/Q4/12/11/md/20251211-101548_Morpheus.md`). The template for these agent reports can be found in `repos/diy-make/reality-merge/md/day_x/`.
        *   After successful processing, move the uncleaned chat log from `.chat/unclean/` to a new `chat/reported_unclean/` directory to prevent re-processing.

3.  **Create Personal Log:**
    *   The agent will create its own "reported unclean" markdown file for the current session in its designated daily `memory/md/` folder. This file will serve as a log of its own activities for the day.

### Step 3: Await Further Instructions

Once the daily reporting and log processing tasks are complete, the agent will commit its work to the `memory/` repository and await further instructions from the user.

## Future Integration with DSPy:

This new workflow will be orchestrated using DSPy to enhance its reliability and consistency.

*   **DSPy for Git Commits:** A DSPy program will be developed to wrap all Git commit operations. This program will ensure that:
    1.  The `detect-secrets` pre-commit hook is always run.
    2.  The agent's local Git `user.name` and `user.email` are correctly configured before every commit.
*   **DSPy for Daily Workflow:** The entire daily workflow described above will be implemented as a DSPy program. This will allow for:
    *   **Structured Task Execution:** Each step of the workflow will be a DSPy `Module`.
    *   **Automated Error Handling:** If a step fails (e.g., a chat log cannot be parsed), the DSPy program can use this as a signal to try a different approach or to alert the user.
    *   **Continuous Optimization:** Over time, the DSPy program can be optimized to make the daily reporting process more efficient and accurate.

This gameplan represents a significant step forward in the evolution of our AI swarm, creating a more robust, intelligent, and self-documenting system for collaborative AI development.