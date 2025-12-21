# WeDo Job: PNG Journaling Batch 2 (Lumina)

## Metadata
- **Description:** Processing and journaling 215 new PNG screenshots.
- **Version:** 1.0
- **Preferred_Agent:** Lumina
- **Reason:** Continuing automated organization of the memory module.

## Workflow
- [x] [PREP-01] **STEP 1:** `list_directory` of the source `png/` inbox.
- [ ] [PREP-02] **STEP 2:** `list_directory` of all existing daily `png/` archives to build a count of files per day.

- [ ] [WORK-01] **LOOP** through source images:
    - [ ] [WORK-01a] **STEP 3a:** `parse` the creation date from the source filename.
    - [ ] [WORK-01b] **STEP 3b:** `read_file` to analyze the image content.
    - [ ] [WORK-01c] **STEP 3c:** `PRESENT` the analysis (automated description and takeaway).
    - [ ] [WORK-01d] **STEP 3d:** `increment` the file count for the parsed date.
    - [ ] [WORK-01e] **STEP 3e:** `run_shell_command` to `mv` the source file.
    - [ ] [WORK-01f] **STEP 3f:** `append_file` to the correct daily journal.

- [ ] [POST-01] **STEP 4:** `dspy_commit` every 10 pictures.
