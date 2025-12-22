# WeDo: Boilerplate Report Schema Thread

## Schema Definition
A standard report in the Metagit environment should follow this hierarchical structure to ensure "Crystallization" of thought:

1. **Title & Meta:** Title, Date, Agent Identity, User Identity, and Project/Branch context.
2. **Executive Summary:** High-level overview of the session or task.
3. **Core Analysis/Metrics:** Structured data (Time, Velocity, Capacities, or Repository changes).
4. **Resources/Context:** Links to internal Git artifacts and external references.
   - **Requirement:** Every location MUST reference both **localhost** (local absolute path) and **remotehost** (GitHub URL).
   - **Requirement:** For Pull Synthesis, list ALL changes and requests directly from the source pull request.
5. **Dynamics & Learnings:** Narrative on collaboration (HITL), corrections, and "Hard-Won Knowledge."
6. **Artifacts:** Visuals (PNGs) or code snippets generated.
7. **Next Steps:** WeDo task list for the singular thread.

## Presentation Protocol
**Direct Aesthetic:** Reports must be presented to the User "straightup"—no triple-backtick Markdown wrappers or line numbers. Use plain text formatting with clear headers and bolding that renders cleanly in the terminal for screenshots and manual copying.

## Tasks
- [ ] WeDo: SCH-BPR-01 | Create standardized Markdown template for reports
  - ID: SCH-BPR-01
  - Status: [ ]
  - Description: Create a reusable template file in schemas/ for future reports to pull from.
- [ ] WeDo: SCH-BPR-02 | Integrate schema check into Pull Synthesis Report
  - ID: SCH-BPR-02
  - Status: [ ]
  - Description: Ensure WEDO-SYN-04 specifically references this schema.
