# WeDo Schema Report

**A. WEDO PSEUDOLANGUAGE SCHEMA**
    **Name:** WeDo Pseudolanguage Schema
    **Version:** 1.0.0
    **Description:** Defines the structure for a task within the 'WeDo' singular thread of user-agent collaboration. This schema formalizes the 'todo.md' as a machine-readable instruction set.

**B. TASK STRUCTURE**
    **Type:** Object
    **Properties:**
        1.  **ID:**
            **Type:** String
            **Description:** A unique, sequential, and human-readable identifier for the task step (e.g., 'WEDO-01', 'IMG-02a'). This is the primary key for tracking progress.
        2.  **DESCRIPTION:**
            **Type:** String
            **Description:** A clear, concise description of the task to be performed.
        3.  **STATUS:**
            **Type:** String
            **Enum:** [ ] = Pending, [x] = Complete, [-] = Skipped/Cancelled.
            **Description:** The current state of the task.
        4.  **COMMAND:** (Optional)
            **Type:** String
            **Description:** The specific shell command or tool call associated with the task.
        5.  **DEPENDENCIES:** (Optional)
            **Type:** Array of Strings
            **Description:** A list of task IDs that must be completed before this task can begin.
    **Required Fields:** ID, DESCRIPTION, STATUS

**C. EXAMPLE**
    **ID:** IMG-03f
    **Description:** Append analysis to the daily PNG journal.
    **Status:** [ ]
    **Command:** cat <<'EOF' >> .../2025-12-18_png_journal.md ...
    **Dependencies:** [IMG-03e]
