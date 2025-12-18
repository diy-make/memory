# WeDo Job Boilerplate: PNG Journal

## Metadata
- **Description:** A generic template for a PNG Journaling WeDo job.
- **Version:** 2.0
- **Preferred_Agent:** [e.g., gemini-2.5-flash]
- **Reason:** [e.g., Sufficient for this task's complexity]

## Workflow
- [ ] [PREP-01] **STEP 1:** `list_directory` of the source `png/` inbox.
- [ ] [PREP-02] **STEP 2:** `list_directory` of all existing daily `png/` archives to build a count of files per day.

- [ ] [WORK-01] **LOOP** through source images:
    - [ ] [WORK-01a] **STEP 3a:** `parse` the creation date (e.g., "2025-12-11") from the source filename.
    - [ ] [WORK-01b] **STEP 3b:** `read_file` to analyze the image content.
        - **ERROR HANDLING:** Implement a try-catch mechanism for image analysis. If an `API Error: Provided image is not valid` or similar occurs, log the error and the filename, then skip to the next image.
    - [ ] [WORK-01c] **STEP 3c:** `INFER` a descriptive name and key takeaway.
        - **ERROR HANDLING:** If image analysis failed or returned invalid data, skip inference for this image and proceed to the next iteration.
    - [ ] [WORK-01d] **STEP 3d:** `increment` the file count for the parsed date to get the new sequential number (e.g., "05").
    - [ ] [WORK-01e] **STEP 3e:** `run_shell_command` to `mv` the source file to its final, sequentially numbered name in the correct daily archive (e.g., `.../11/png/05-new-descriptive-name.png`).
    - [ ] [WORK-01f] **STEP 3f:** `append_file` to the correct daily journal (`.../11/md/2025-12-11_png_journal.md`) with the new entry.

- [ ] [POST-01] **STEP 4:** `dspy_commit` all changes to the `public` and `memory` repositories.
