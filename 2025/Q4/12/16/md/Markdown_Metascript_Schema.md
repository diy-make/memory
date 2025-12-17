# Schema: Markdown Metascript (`.todo.md`)

## Concept
A `.todo.md` file acts as both the **definition** of a workflow and the **execution log**. It is a valid Markdown file that uses specific tagging conventions to define tool calls, async operations, variables, and human interactions.

## File Structure

### 1. Header (Metadata)
Every chain must start with a YAML-style frontmatter block (or a clear Markdown table) defining its properties.

```markdown
# Chain: [Chain Name]
**Description:** [Description of what this chain does]
**Inputs:** [list, of, required, inputs]
**Output:** [Name of final output variable]
```

### 2. Task List (The Logic)
The core logic is a standard Markdown task list. I use **Action Tags** (uppercase keywords) to define behavior. Each task must have a unique Index ID (e.g., `[CHAIN-01]`) to allow for mixing and matching.

#### Syntax Guide:

*   **Standard Tool Call:**
    `- [ ] [ID-XX] EXECUTE [Tool Name] inputs={...} output=[var_name]`
*   **Async Operation:**
    `- [ ] [ID-XX] ASYNC [Tool Name] inputs={...} output=[var_name]`
*   **Wait Command:**
    `- [ ] [ID-XX] AWAIT [var_name_1], [var_name_2]`
*   **Human Interaction:**
    `- [ ] [ID-XX] PROMPT "[Question for user?]" output=[response_var]`
*   **Loop:**
    `- [ ] [ID-XX] LOOP [collection_var] as [item_var]:`
        *   (Indented tasks follow standard syntax)
*   **Condition:**
    `- [ ] [ID-XX] IF [condition]:`
        *   (Indented tasks)

## The Schema Definition (as a Reference) 

While the file is Markdown, strict adherence to this structure is required for me to "compile" it into action.

```markdown
# [Chain Name]

## Metadata
- **Description**: ...
- **Version**: 1.0

## Workflow
- [ ] [ID-01] **STEP 1**: [ACTION_TAG] [Tool/Instruction] [Parameters]
```

## Example: `image_description.todo.md`

This is the **actual source file** you would save in `repos/diy-make/memory/public/chains/`.

```markdown
# Chain: Generate Image Descriptions

## Metadata
**Description:** Scans a directory, describes images asynchronously, and creates Markdown files.
**Inputs:** target_directory

## Workflow
- [ ] [IMG-01] **STEP 1:** EXECUTE `list_directory` dir_path={target_directory} output=image_list

- [ ] [IMG-02] **STEP 2:** LOOP image_list as image:
    - [ ] [IMG-02a] **STEP 2a:** ASYNC `read_file` file_path={image} output=desc_raw

- [ ] [IMG-03] **STEP 3:** AWAIT desc_raw (all instances)

- [ ] [IMG-04] **STEP 4:** LOOP image_list as image:
    - [ ] [IMG-04a] **STEP 4a:** PROMPT "Review description for {image}: {desc_raw}. Approve?" output=user_feedback
    - [ ] [IMG-04b] **STEP 4b:** EXECUTE `write_file` file_path="{image}.md" content="# {image}\n{user_feedback}"
```
