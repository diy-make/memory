# AI Swarm Memory System

This `public/` repository is one of three repositories that constitute the collective long-term memory for a swarm of AI agents operating within the `gemini/` local orchestration system. This repository is intended to be a boilerplate that other developers can reuse.

This repository, along with its siblings (`private/` and `drive_only/`), are contained within a parent `memory/` "passthrough" repository, which is ignored by the main `gemini/` project's Git tracking.

## Sub-Repository Structure and Purpose:

The memory system is organized into three distinct sub-repositories:

### 1. `public/` (This Repository)
*   **Purpose:** A version-controlled repository for all public-facing and non-sensitive information related to the swarm's activities. This includes daily summaries, agent reports, and non-sensitive structured data.
*   **Sync Target:** This repository is synced with a public GitHub repository. It is also synced with Google Drive for backup and accessibility.
*   **`.gitignore` Philosophy:** This repository should ideally not contain a `.gitignore` file. Any files that would typically be ignored (e.g., virtual environments, large datasets, temporary files) should be placed in the `drive_only/` repository.

### 2. `private/`
*   **Purpose:** A version-controlled, private GitHub repository for sensitive information that should not be publicly accessible.
*   **Sync Target:** This repository is synced with a private GitHub repository. It is also synced with Google Drive for backup and accessibility.
*   **`.gitignore` Philosophy:** Similar to the `public/` repository, this repository should not contain a `.gitignore` file.

### 3. `drive_only/`
*   **Purpose:** A repository for files that are not suitable for Git version control, but are synced with Google Drive. This is the designated location for:
    *   Large binary files and assets.
    *   Virtual environments (`.venv`).
    *   Temporary files and logs.
    *   Any other files that would typically be included in a `.gitignore` file.
*   **Sync Target:** This repository is synced with Google Drive.

This separation of concerns ensures a clean, organized, and secure system for managing the AI swarm's collective memory, while providing a reusable boilerplate for other projects.