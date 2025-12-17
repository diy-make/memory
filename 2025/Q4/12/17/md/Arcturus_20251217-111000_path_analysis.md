# Report: Configuration & Path Consistency Analysis

**Date:** 2025-12-17
**Agent:** Arcturus

## Objective
To identify files within `repos/diy-make/memory/public/json/` that are failing to utilize the centralized configuration in `local_paths.json` and are instead relying on hardcoded or legacy paths (specifically `.chat/unclean/` and `.chat/comms/`).

## Findings

### 1. Centralized Configuration
The file `repos/diy-make/memory/public/json/local_paths.json` is correctly defined with V1 path standards:
- `chat_history`: "dynamic/stream/"
- `swarm_comms`: "repos/diy-make/memory/comms/"
- `used_agent_names`: "repos/diy-make/memory/used_agent_names.json"

### 2. Violations & Legacy Path usage

#### A. `startup_protocol.json`
- **Issue:** Uses hardcoded legacy path `.chat/unclean/`.
- **Location:** Steps "Identify Active Chats" and "Read Previous Session Log".
- **Impact:** Agents adhering strictly to this protocol will look in the wrong directory for chat logs, failing to identify active sessions or read previous context.

#### B. `rules/swarm_protocol.json`
- **Issue:** Uses hardcoded V1 paths instead of referencing variables from `local_paths.json`.
- **Location:**
    - "Triggered Mode" -> `repos/diy-make/memory/comms/`
    - "Announce Existence" -> `repos/diy-make/memory/comms/`
    - "Name Uniqueness" -> `repos/diy-make/memory/used_agent_names.json`
- **Impact:** While functionally correct for now, this creates technical debt. Any future changes to directory structure would require hunting down these hardcoded strings rather than updating the single config file.

## Remediation Plan
1.  **Update `startup_protocol.json`**: Replace `.chat/unclean/` references with instructions to look in the directory defined by `local_paths.json` (key: `chat_history`).
2.  **Update `rules/swarm_protocol.json`**: Replace hardcoded paths with references to `local_paths.json` keys (`swarm_comms`, `used_agent_names`).

## Status
- [x] Report Generated
- [x] Fixes Applied
