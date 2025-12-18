# WeDo Job: Vigil's PNG Refactoring Takeover (from Pragma)

## Metadata
- **Description:** Continuation of the automated PNG refactoring job. Processes images from the inbox, renames them, moves them to date-based archives, and updates daily journals.
- **Version:** 2.1 (Strict Format)
- **Preferred_Agent:** `gemini-2.5-flash`
- **Reason:** Standardized refactoring task with specific formatting requirements.
- **Model Suggestion:**
    - **Manual Phase:** Suggest user run `/model gemini-3` for superior inference.
    - **Automated Phase:** Suggest user run `/model gemini-2.5-flash` for speed and efficiency.

## Progress Tracking
- **Handover from Pragma:** 211 images processed total by previous agents.
- **Remaining in Inbox:** 77 images.
- **Goal for this Session:** Process next batch (up to 50 images).

## Workflow
- [x] [REF-01] **STEP 1:** `list_directory` of the source `public/png/` inbox.
- [x] [REF-02] **STEP 2:** Verify daily journal files exist.
- [ ] [REF-03] **STEP 3: LOOP** through PNGs in the source inbox (Limit 50):
    - [ ] [REF-03a] **STEP 3a:** `parse` the creation date from the filename.
    - [ ] [REF-03b] **STEP 3b:** `read_file` to analyze the image content.
    - [ ] [REF-03c] **STEP 3c:** `PRESENT` the analysis to the user for approval (Manual Mode).
        - **Action:** Display the **Original Filename**, **Proposed Filename**, **Target Path**, **Target Journal Path**, and the **Full Journal Entry**.
        - **Wait:** Do not proceed to Move or Append until user approves.
    - [ ] [REF-03d] **STEP 3d:** `run_shell_command` to `mv` the source file to its final, sequentially numbered name in the correct daily archive.
    - [ ] [REF-03e] **STEP 3e:** `append_file` to the correct daily journal using the **Strict Format**.

### Strict Journal Format:
```markdown
### {{new_sequential_number}}. `{{new_descriptive_filename}}.png`
![{{new_descriptive_filename}}.png](../png/{{new_descriptive_filename}}.png)
- **Description:** {{inferred_description}}
- **Key Takeaway:** {{inferred_key_takeaway}}
- **Creation Date:** {{parsed_creation_date_from_original_filename}}
- **Original Filename:** `{{original_filename}}`
```

- [ ] [GC-01] **GARBAGE COLLECTION (CRITICAL):**
    - **IF count >= 50:** STOP PROCESSING.
    - **ACTION:** Perform [POST-01] commit.
    - **ACTION:** Update this job file to mark progress.
    - **ACTION:** TERMINATE SESSION (Exit).
- [ ] [POST-01] **STEP 4:** `dspy_commit` all changes every 5 images.
