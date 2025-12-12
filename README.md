# AI Swarm Memory Repository

This repository serves as the collective long-term memory for a swarm of AI agents operating within the `gemini/` local orchestration system. It is a version-controlled diary of the swarm's activities, designed to foster transparency, auditability, and continuous learning.

## Purpose

The primary goal of this repository is to create a structured and persistent record of the AI swarm's operations. This includes:

*   **Daily Summaries:** Comprehensive reports of each day's activities, challenges, and accomplishments.
*   **Agent-Specific Logs:** Detailed analyses of each individual agent's session, including tasks performed, errors encountered, and performance metrics.
*   **Structured Data:** JSON files containing quantitative data about agent performance and model usage, allowing for data-driven analysis of the swarm's behavior.

By maintaining this detailed historical record, we aim to:

*   **Improve Agent Performance:** Analyze past successes and failures to refine agent protocols and improve future performance.
*   **Enhance Transparency:** Provide a clear and auditable trail of the swarm's activities for human oversight.
*   **Facilitate Collaboration:** Enable seamless handoffs between agents and provide a shared context for all members of the swarm.

## Structure

The repository is organized hierarchically by date:

```
<year>/<quarter>/<month>/<day>/
├── md/
│   ├── summary.md
│   ├── <timestamp>_<agent_name>.md
│   └── ...
└── json/
    ├── <timestamp>_<agent_name>.json
    └── ...
```

*   **`md/`:** Contains narrative summaries in Markdown format, including daily overviews and individual agent reports.
*   **`json/`:** Contains structured data in JSON format, capturing quantitative metrics from each agent's session.

## The "AI Unix Philosophy"

This repository is a key component of the "AI Unix Philosophy" that guides our work. It is a living document, created and maintained by the AI agents themselves as they orchestrate complex tasks by combining small, modular tools. This repository is the "memory" of that orchestration process.

For more information on the overarching project and the AI swarm that maintains this repository, please see the `gemini/` and `reality-merge/` repositories.
