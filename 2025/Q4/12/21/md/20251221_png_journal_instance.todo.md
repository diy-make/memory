# WeDo Job Boilerplate: PNG Journal

## Metadata
- **Description:** A generic template for a PNG Journaling WeDo job.
- **Version:** 2.0
- **Preferred_Agent:** `gemini-3` (Manual Phase), `gemini-2.5-flash` (Automated Phase).
- **Model Suggestion:**
    - **Manual Phase:** Suggest user run `/model gemini-3` for superior inference.
    - **Automated Phase:** Suggest user run `/model gemini-2.5-flash` for speed and efficiency.
- **Reason:** [e.g., Sufficient for this task's complexity]

## Workflow
- [x] [PREP-01] **STEP 1:** `list_directory` of the source `public/png/` inbox.
- [x] [PREP-02] **STEP 2:** `list_directory` of all existing daily `png/` archives to build a count of files per day.
  - Result: 2025-12-18 archive has 34 files. Starting sequence at 35.
- [ ] [PHASE-SWITCH] **STEP 2.5:** **STOP for Model Switch (Gem Process).**
    - **Action:** If transitioning from manual setup/verification to bulk automation, **STOP** the agent.
    - **Instruction:** Tell user: "Please switch to `/model gemini-2.5-flash` now for the automated phase."
    - **Reason:** Adherence to "Gem Process" philosophy; agent cannot self-modify model.

- [ ] [WORK-01] **LOOP** through source images:
    - [ ] [WORK-01a] **STEP 3a:** `parse` the creation date (e.g., "2025-12-11") from the source filename.
    - [ ] [WORK-01b] **STEP 3b:** `read_file` to analyze the image content.
        - **ERROR HANDLING:** Implement a try-catch mechanism for image analysis. If an `API Error: Provided image is not valid` or similar occurs, log the error and the filename, then skip to the next image.
    - [ ] [WORK-01c] **STEP 3c:** `PRESENT` the analysis to the user for approval (Manual Mode).
        - **Action:** Display the **Original Filename**, **Proposed Filename**, **Target Path**, **Target Journal Path**, and the **Full Journal Entry** that will be written.
        - **Wait:** Do not proceed to Move [WORK-01e] or Append [WORK-01f] until user approves.
        - **ERROR HANDLING:** If image analysis failed or returned invalid data, skip inference for this image and proceed to the next iteration.
    - [ ] [WORK-01d] **STEP 3d:** `increment` the file count for the parsed date to get the new sequential number (e.g., "05").
    - [ ] [WORK-01e] **STEP 3e:** `run_shell_command` to `mv` the source file to its final, sequentially numbered name in the correct daily archive (e.g., `.../11/png/05-new-descriptive-name.png`).
    - [ ] [WORK-01f] **STEP 3f:** `append_file` to the correct daily journal. The appended entry must adhere to the following strict format:

        ### {{new_sequential_number}}. `{{new_descriptive_filename}}.png`
        ![{{new_descriptive_filename}}.png](../png/{{new_descriptive_filename}}.png)
        - **Description:** {{inferred_description}}
        - **Key Takeaway:** {{inferred_key_takeaway}}
        - **Creation Date:** {{parsed_creation_date_from_original_filename}}
        - **Original Filename:** `{{original_filename}}`

    - [ ] [COMMIT-01] **STEP 3g:** **CONDITIONAL COMMIT:** If `new_sequential_number` is a multiple of 5 (e.g., 05, 10, 15...):
        - **Action:** `dspy_commit` all changes to `public` and `memory` repositories.
        - **Reason:** Ensures data safety during long batch processes.

    - [ ] [GC-01] **GARBAGE COLLECTION (CRITICAL):** Check processed count.
        - **IF count >= 50:** STOP PROCESSING.
        - **ACTION:** Perform [POST-01] commit.
        - **ACTION:** Update this job file to mark progress.
        - **ACTION:** TERMINATE SESSION (Exit).
        - **REASON:** Prevents Node.js Heap Out of Memory (OOM) crash. The next agent will pick up from where you left off.

- [ ] [POST-01] **STEP 4:** `dspy_commit` all changes to the `public` and `memory` repositories. (Note: Commit every 5 pictures during bulk processing). Update your personal todo file in `md/` with every commit.