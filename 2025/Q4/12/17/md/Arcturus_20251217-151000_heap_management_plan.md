# Arcturus Heap Management & Garbage Collection Strategy

**Date:** 2025-12-17
**Agent:** Arcturus

## Objective
To prevent session termination due to `JavaScript heap out of memory` errors (as encountered by Agent Thalos) by implementing proactive resource management.

## Strategies

### 1. Atomic Operations
- **Method:** Break large code modifications into smaller, targeted `replace` calls instead of full-file rewrites.
- **Benefit:** Reduces the memory footprint of file buffers within the Node.js execution environment.

### 2. Context Window Monitoring
- **Method:** Monitor the remaining context window percentage. 
- **Trigger:** Alert the user if the window drops below 40%, per Swarm Protocol.
- **Benefit:** Prevents internal state bloat that hinders efficient garbage collection.

### 3. Stream-Optimized File Access
- **Method:** Use `limit`/`offset` for large file reads and shell-based filters (`grep`, `tail`, `awk`) for initial data extraction.
- **Benefit:** Avoids loading excessive data into the JavaScript heap.

### 4. Memory-Conscious Tooling
- **Method:** Limit recursive searches to specific sub-repositories when possible rather than searching the entire metagit root.
- **Benefit:** Keeps search result objects small and manageable.

### 5. Proactive Session Refresh
- **Method:** Periodically monitor process memory via `ps`. If heap usage approaches 4GB, recommend starting a new chat log to clear the session state.
