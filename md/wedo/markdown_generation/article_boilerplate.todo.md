# WeDo Template: Article Boilerplate Schema

## Schema Definition
An article in the Metagit environment should follow this narrative-driven structure:

1. **Title & Byline:** Engaging Title, Date, Agent Identity (Author), and Context.
2. **The Narrative Hook:** An opening that sets the scene (e.g., an event, a conflict, or a realization).
3. **The Core Thesis:** The main argument or discovery being shared.
4. **Key Thematic Threads:** Detailed exploration of the topic, incorporating:
   - **Historical Context:** How we got here.
   - **Technical/Architectural Deep-Dive:** The "Calculus of Events" or specific mechanics.
   - **Collaborative Dynamics:** The human-agent interaction (HITL).
     - **Boomerang Principle:** Identify deviations from user intent and how they were resolved.
     - **Synaptic Principle:** Highlight moments where human-agent "synapses" fired—where feedback redefined the narrative or technical path.
5. **Visual Evidence:** Integration of PNG Journal artifacts with descriptive captions.
6. **Conclusion & Vision:** Synthesis of the findings and a look towards the future.
7. **Resources & Context:** Links to internal Git artifacts and external references (Localhost/Remotehost).

## Presentation Protocol
**Narrative Aesthetic:** Articles should be written for a broader audience than reports. Use evocative language while maintaining technical precision. No triple-backtick Markdown wrappers. Use clear headers and bolding for emphasis.
**Iteration Mandate:** Each subsequent draft of an article MUST have a higher word count than the previous version, ensuring increasing narrative depth and complexity as the story crystallizes.
**Storage Protocol:** 
- **Working Drafts:** Store in `md/context/` with timestamped filenames (e.g., `Pytheas_20251228-174500_SeedTree_v4.md`).
- **Final Versions:** Store in the root `md/` of the temporal branch with user-friendly filenames (e.g., `SeedTree_Gemini_CLI_Investment_Case.md`).
