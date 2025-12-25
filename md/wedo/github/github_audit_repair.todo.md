# WeDo Template: GitHub Audit & Repair

## Process Protocol
**GitHub Audit & Repair:** Systematically scanning local and remote repositories for broken links, verifying file structure integrity (e.g., Type Attribution Leafs), and performing high-fidelity repairs to ensure documentation accuracy and terminal readability.

## Requirements
1. **Audit Script:** Must use a deterministic script (Python preferred) to identify broken image and markdown links.
2. **Remote Verification:** Must use `web_fetch` or `browse` to confirm that local fixes are reflected on the GitHub remote.
3. **Type Integrity:** Must verify that files are in their appropriate "attribution leafs" (e.g., .jpg in jpg/, .png in png/).
4. **Manifest Synchronization:** Must regenerate any project-specific media manifests (e.g., `media_count.md`).

## Tasks
- [ ] WeDo: GHA-AUD-01 | Execute Comprehensive Audit Script
  - ID: GHA-AUD-01
  - Status: [ ]
  - Description: Scan all markdown files for broken image and cross-reference links.
- [ ] WeDo: GHA-FIX-02 | Perform High-Fidelity Repairs
  - ID: GHA-FIX-02
  - Status: [ ]
  - Description: Fix paths, rename files, and reconcile extensions according to type mandates.
- [ ] WeDo: GHA-VER-03 | Verify Remote Synchronization
  - ID: GHA-VER-03
  - Status: [ ]
  - Description: Use web tools to confirm that remote main reflects the repaired state.
- [ ] WeDo: GHA-MAN-04 | Synchronize Media Manifest
  - ID: GHA-MAN-04
  - Status: [ ]
  - Description: Regenerate the media index to ensure all links are valid and tracked.
