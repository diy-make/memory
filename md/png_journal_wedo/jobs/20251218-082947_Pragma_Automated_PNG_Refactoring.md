# WeDo Job: Refactor and Journal all PNGs

## Metadata
- **Description:** Iterates through all PNGs in the `public/png/` inbox. For each, parses the date, renames it sequentially for that date, moves it to the correct daily archive. Appends a new journal entry to the correct daily journal file.
- **Version:** 1.0
- **Preferred_Agent:** `gemini-exp-1206`
- **Reason:** This is a complex, one-off refactoring task that requires careful file manipulation and dynamic path generation.

## Workflow
- [ ] [REF-01] **STEP 1:** `list_directory` of the source `public/png/` inbox.
- [x] [REF-02] **STEP 2:** For each day (Dec 11, 12, 13, 14, 15):
    - [x] [REF-02a] **STEP 2a:** Create the daily journal file for that day.
- [ ] [REF-03] **STEP 3:** LOOP through all PNGs in the source inbox:
    - [x] Processed 211 images (80-89 for 2025-12-15, 01-38 for 2025-12-16, 01-170 for 2025-12-17).
    - [ ] [REF-03a] **STEP 3a:** `parse` the creation date from the filename.
    - [ ] [REF-03b] **STEP 3b:** `list_directory` of the target daily `png/`
    - [ ] [REF-03c] **STEP 3c:** `read_file` to analyze the image content.
    - [ ] [REF-03d] **STEP 3d:** `INFER` a descriptive name and key takeaway.
    - [ ] [REF-03e] **STEP 3e:** `run_shell_command` to `mv` the source file to its final, sequentially numbered name in the correct daily archive.
    - [ ] [REF-03f] **STEP 3f:** `append_file` to the correct daily journal.

- [x] [GC-01] **GARBAGE COLLECTION (CRITICAL):** Check processed count in current session.
    - **IF count >= 50:** STOP PROCESSING.
    - **ACTION:** Perform [POST-01] commit.
    - **ACTION:** Update this job file to mark progress.
    - **ACTION:** TERMINATE SESSION (Exit).
    - **REASON:** Prevents Node.js Heap Out of Memory (OOM) crash.
- [ ] [POST-01] **STEP 4:** `dspy_commit` all changes.
