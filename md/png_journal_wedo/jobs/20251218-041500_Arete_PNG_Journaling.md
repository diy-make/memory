# WeDo Job: PNG Journaling (Arete)

## Metadata
- **Description:** Processing and journaling 223 new PNG screenshots from the public/png/ inbox.
- **Version:** 1.0
- **Preferred_Agent:** Arete
- **Reason:** Continuing the work of Lumina with updated protocol requirements.

## Workflow
- [x] [PREP-01] **STEP 1:** `list_directory` of the source `public/png/` inbox. (223 files found).
- [ ] [PREP-02] **STEP 2:** `list_directory` of all existing daily `png/` archives to build a count of files per day.

- [ ] [WORK-01] **LOOP** through source images:
    - [x] Processed 51 images (80-89 for 2025-12-15, 01-38 for 2025-12-16, 01-03 for 2025-12-17).
    - [ ] [WORK-01a] **STEP 3a:** `parse` the creation date from the source filename.
    - [ ] [WORK-01b] **STEP 3b:** `read_file` to analyze the image content.
        - **ERROR HANDLING:** Log and skip if "Provided image is not valid".
    - [ ] [WORK-01c] **STEP 3c:** `PRESENT` the analysis (Original Filename, Description, Takeaway, Reorganization, Journal Path).
    - [ ] [WORK-01d] **STEP 3d:** `increment` the file count for the parsed date.
    - [ ] [WORK-01e] **STEP 3e:** `run_shell_command` to `mv` the source file.
    - [ ] [WORK-01f] **STEP 3f:** `append_file` to the correct daily journal.

- [ ] [POST-01] **STEP 4:** `dspy_commit` every 10 pictures. Update personal todo file with every commit.
