# WeDo Template: Boilerplate Report Schema

## Schema Definition
A standard report in the Metagit environment should follow this hierarchical structure:

1. **Title & Meta:** Title, Date, Agent Identity, User Identity, and Project/Branch context.
2. **Executive Summary:** High-level overview of the session or task.
3. **Core Analysis/Metrics:** Structured data (Time, Velocity, Capacities, or Repository changes).
4. **Resources/Context:** Links to internal Git artifacts and external references.
   - **Dual Referencing:** Every location MUST reference both **localhost** and **remotehost**.
   - **Audit Scrutiny:** For Pull Synthesis, list ALL changes and requests directly from the source. Document resolutions in granular detail to ensure a transparent legislative history.
   - **Active Investigation:** Document the verification of any referenced artifacts (e.g., gifs, links) on the **localhost**.
5. **Dynamics & Learnings:** Narrative on collaboration (HITL), corrections, and "Hard-Won Knowledge."
6. **Artifacts:** Visuals (PNGs) or code snippets generated.
7. **Next Steps:** WeDo task list for the singular thread.

## Presentation Protocol
**Direct Aesthetic:** Reports must be presented to the User "straightup"—no triple-backtick Markdown wrappers. Use plain text with clear headers and bolding.