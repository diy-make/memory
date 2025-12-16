# TODO: Refactor Chat Processing & Summarization Pipeline

- [ ] **1. Refactor `parse_chat_log.py`**
    - [ ] Modify the script to accept the path to `parsing_config.json` as a command-line argument.
- [ ] **2. Refactor `dspy_chat_summarizer.py`**
    - [ ] Ensure the script outputs a clean JSON object to standard output.
- [ ] **3. Refactor `dspy_daily_summary_generator.py`**
    - [ ] Modify the script to read JSON from standard input and write markdown to standard output.
- [ ] **4. Rewrite `dspy_daily_workflow_orchestrator.py`**
    - [ ] Change the script to accept `dynamic/stream` and memory module paths as arguments.
    - [ ] Import the other scripts as modules instead of using `subprocess`.
    - [ ] Pass data between modules as Python objects.
    - [ ] The orchestrator will handle all file I/O.
- [ ] **5. Test the new pipeline**
    - [ ] Run the refactored orchestrator and verify that it correctly processes logs and generates the summary reports.
- [ ] **6. Connect to a real `dspy` model (Future Task)**
    - [ ] Investigate and implement the correct way to configure and use `dspy` with a real language model.
