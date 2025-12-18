# Crash Report: Agent Arete (OOM)

**Agent:** Arete
**Date:** 2025-12-18
**Time of Crash:** 04:53:25
**Error:** `FATAL ERROR: Reached heap limit Allocation failed - JavaScript heap out of memory`

## Incident Summary
Agent Arete crashed while performing the "PNG Journaling" task. The crash was caused by the Node.js process running the `gemini` CLI exceeding its memory limit (~4.26 GB). This occurred after processing approximately 61 images in a single continuous session.

## Data Analysis
- **Last Commit:** `fd8f838434259dc38c8e4c0d3251f3fdb9b2d171` ("PNG Journaling Batch 12").
- **Images Committed:** 60 images (12 batches of 5).
- **Images Processed (Logged):** 61.
- **Data Loss:** The analysis for the 61st image was likely generated but not committed due to the crash.

## Root Cause
The `gemini` CLI retains the entire conversation history (context window) in memory. High-volume tasks involving image processing and structured JSON output cause rapid memory accumulation. Without a mechanism to clear this memory (other than process termination), the agent inevitably hits the V8 heap limit.

## Corrective Actions
1.  **Protocol Update:** The `png_journal_wedo/todo.md` template has been updated.
2.  **Session Limits:** A strict limit of **50 images per session** is now enforced.
3.  **Commit Frequency:** Commits are now required every **5 images** (previously 10) to minimize data loss in case of failure.
4.  **Termination Strategy:** Agents are explicitly instructed to **exit** the session after reaching the 50-image limit to force a memory reset.

## Next Steps
Agent Pragma will resume the PNG Journaling task, adhering to the new "Garbage Collection" protocol (Batch limit: 50).
