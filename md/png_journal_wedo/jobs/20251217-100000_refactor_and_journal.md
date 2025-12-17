# WeDo Job: Refactor and Journal all PNGs

## Metadata
- **Description:** 1. Iterates through all PNGs in the `png/` inbox. 2. For each, parses the date, renames it sequentially for that date, moves it to the correct daily archive. 3. Appends a new journal entry to the correct daily journal file.
- **Version:** 1.0
- **Preferred_Agent:** gemini-exp-1206
- **Reason:** This is a complex, one-off refactoring task that requires careful file manipulation and dynamic path generation.

## Workflow
- [ ] [REF-01] **STEP 1:** `list_directory` of the source `png/` inbox.
- [ ] [REF-02] **STEP 2:** For each day (Dec 11, 12, 13, 14, 15):
    - [ ] [REF-02a] **STEP 2a:** Create the daily journal file for that day.
- [ ] [REF-03] **STEP 3:** LOOP through all PNGs in the source inbox:
    - [ ] [REF-03a] **STEP 3a:** `parse` the creation date from the filename.
    - [ ] [REF-03b] **STEP 3b:** `list_directory` of the target daily `png/` archive to get the current file count for sequential naming.
    - [ ] [REF-03c] **STEP 3c:** `read_file` to analyze the image content.
    - [ ] [REF-03d] **STEP 3d:** `INFER` a descriptive name and key takeaway.
    - [ ] [REF-03e] **STEP 3e:** `run_shell_command` to `mv` the source file to its final, sequentially numbered name in the correct daily archive.
    - [ ] [REF-03f] **STEP 3f:** `append_file` to the correct daily journal.

- [ ] [POST-01] **STEP 4:** `dspy_commit` all changes.
