# WeDo Job Boilerplate: PNG Journal

## Metadata
- **Description:** A generic template for a PNG Journaling WeDo job.
- **Version:** 2.0
- **Preferred_Agent:** `gemini-3` (for initial setup/manual phases), transitioning to `gemini-2.5-flash` (for established, automated processes)
- **Reason:** [e.g., Sufficient for this task's complexity]

## Workflow
- [ ] [PREP-01] **STEP 1:** `list_directory` of the source `public/png/` inbox.
- [ ] [PREP-02] **STEP 2:** `list_directory` of all existing daily `png/` archives to build a count of files per day.

- [ ] [WORK-01] **LOOP** through source images:
    - [ ] [WORK-01a] **STEP 3a:** `parse` the creation date (e.g., "2025-12-11") from the source filename.
    - [ ] [WORK-01b] **STEP 3b:** `read_file` to analyze the image content.
        - **ERROR HANDLING:** Implement a try-catch mechanism for image analysis. If an `API Error: Provided image is not valid` or similar occurs, log the error and the filename, then skip to the next image.
    - [ ] [WORK-01c] **STEP 3c:** `PRESENT` the analysis to the user for approval using the following format:
        - **Original Filename:** The name of the file before processing.
        - **Description:** A detailed narrative of what is shown in the image.
        - **Key Takeaway:** The core insight or action derived from the image.
        - **Proposed Reorganization:** New filename and target directory.
        - **Journal Path:** The specific daily journal file to be updated (including a Markdown link to the image).
    - [ ] [WORK-01d] **STEP 3d:** `increment` the file count for the parsed date to get the new sequential number (e.g., "05").
    - [ ] [WORK-01e] **STEP 3e:** `run_shell_command` to `mv` the source file to its final, sequentially numbered name in the correct daily archive (e.g., `.../11/png/05-new-descriptive-name.png`).
    - [ ] [WORK-01f] **STEP 3f:** `append_file` to the correct daily journal. The appended entry must adhere to the following strict format:

        ### {{new_sequential_number}}. `{{new_descriptive_filename}}.png`
        ![{{new_descriptive_filename}}.png](../../png/{{new_descriptive_filename}}.png)
        - **Description:** {{inferred_description}}
        - **Key Takeaway:** {{inferred_key_takeaway}}
        - **Creation Date:** {{parsed_creation_date_from_original_filename}}
        - **Original Filename:** `{{original_filename}}`

    - [ ] [GC-01] **GARBAGE COLLECTION (CRITICAL):** Check processed count.
        - **IF count >= 50:** STOP PROCESSING.
        - **ACTION:** Perform [POST-01] commit.
        - **ACTION:** Update this job file to mark progress.
        - **ACTION:** TERMINATE SESSION (Exit).
        - **REASON:** Prevents Node.js Heap Out of Memory (OOM) crash. The next agent will pick up from where you left off.

- [ ] [POST-01] **STEP 4:** `dspy_commit` all changes to the `public` and `memory` repositories. (Note: Commit every 5 pictures during bulk processing). Update your personal todo file in `md/` with every commit.