# Chain: Generate Image Descriptions
- [ ] WeDo: this looks old and chains/ should be removed. Likely an artifact as we figured out the WeDo system.
## Metadata
**Description:** Scans a directory, describes images using `read_file`, and creates Markdown files.
**Inputs:** target_directory

## Workflow
- [ ] [IMG-01] **STEP 1:** EXECUTE `list_directory` dir_path={target_directory} output=image_list

- [ ] [IMG-02] **STEP 2:** LOOP image_list as image:
    - [ ] [IMG-02a] **STEP 2a:** IF image ends with ".png":
        - [ ] [IMG-02aa] **STEP 2aa:** EXECUTE `py/validate_png.py` file_path="{target_directory}/{image}"
            - [ ] **ON_ERROR:** LOG "Skipping corrupt PNG: {image}" AND CONTINUE_LOOP
        - [ ] [IMG-02b] **STEP 2b:** EXECUTE `read_file` file_path="{target_directory}/{image}" output=desc_raw
        - [ ] [IMG-02c] **STEP 2c:** PROMPT "Review description for {image}: {desc_raw.description}. Approve or Edit?" output=user_feedback
        - [ ] [IMG-02d] **STEP 2d:** EXECUTE `write_file` file_path="{target_directory}/{image}.md" content="# {image}\n\n![{image}]({image})\n\n*{user_feedback}*\n"
