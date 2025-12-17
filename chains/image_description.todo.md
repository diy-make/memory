# Chain: Generate Image Descriptions

## Metadata
**Description:** Scans a directory, describes images using `read_file`, and creates Markdown files.
**Inputs:** target_directory

## Workflow
- [ ] [IMG-01] **STEP 1:** EXECUTE `list_directory` dir_path={target_directory} output=image_list

- [ ] [IMG-02] **STEP 2:** LOOP image_list as image:
    - [ ] [IMG-02a] **STEP 2a:** IF image ends with ".png":
        - [ ] [IMG-02b] **STEP 2b:** EXECUTE `read_file` file_path="{target_directory}/{image}" output=desc_raw
        - [ ] [IMG-02c] **STEP 2c:** PROMPT "Review description for {image}: {desc_raw.description}. Approve or Edit?" output=user_feedback
        - [ ] [IMG-02d] **STEP 2d:** EXECUTE `write_file` file_path="{target_directory}/{image}.md" content="# {image}\n\n![{image}]({image})\n\n*{user_feedback}*\n"
