# Vigil's Plan for Automated PNG Refactoring Takeover

## Context
I am taking over the "Automated PNG Refactoring" task from Agent Pragma, who terminated their session due to memory constraints. 77 images remain in the `public/png` inbox. Pragma recently updated the job boilerplate with a specific strict format for journal entries.

## Objectives
1.  **Process Next Batch:** Process a maximum of 50 images from the `public/png` inbox to prevent memory exhaustion.
2.  **Strict Formatting:** Apply the newly defined journal entry format for all processed images.
3.  **Journaling:** Move images to their correct daily archives and append entries to the corresponding daily journal files.

## Detailed Plan

### 1. Verification & Setup
-   **Verify Boilerplate:** Confirm the content of `repos/diy-make/memory/public/md/png_journal_wedo/todo.md` matches the new format requirements.
-   **Create Job File:** Generate a new job file `repos/diy-make/memory/public/md/png_journal_wedo/jobs/20251218-115000_Vigil_Automated_PNG_Refactoring.md` incorporating the latest protocols.

### 2. Execution Loop (Limit: 50 Images)
For each image in the inbox:
1.  **Parse Date:** Extract the date from the filename (e.g., `Screenshot from 2025-12-17...`).
2.  **Analyze:** Read the image to understand its content.
3.  **Infer Metadata:** Generate a descriptive filename, description, and key takeaway.
4.  **Targeting:** Determine the correct destination directory (`.../YYYY/Q#/MM/DD/png/`) and journal file (`.../YYYY/Q#/MM/DD/md/YYYY-MM-DD_png_journal.md`).
5.  **Move:** Rename and move the file to the destination.
6.  **Journal:** Append the entry to the journal file using the **Strict Format**:
    ```markdown
    ### {{new_sequential_number}}. `{{new_descriptive_filename}}.png`
    ![{{new_descriptive_filename}}.png](../../png/{{new_descriptive_filename}}.png)
    - **Description:** {{inferred_description}}
    - **Key Takeaway:** {{inferred_key_takeaway}}
    - **Creation Date:** {{parsed_creation_date_from_original_filename}}
    - **Original Filename:** `{{original_filename}}`
    ```
7.  **Commit:** Perform a git commit every 5 processed images to ensure safety and progress tracking.

### 3. Termination
-   **Garbage Collection:** Upon reaching 50 processed images, I will stop processing, update the job file, and terminate the session to allow a fresh agent to handle the remaining files.
