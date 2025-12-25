# WeDo Protocol: Visual-Text Parity Audit

## Process Protocol
**Audit Objective:** To ensure absolute fidelity between the visual record (PNG files) and the textual record (Markdown descriptions) within the swarm's chronological memory. This protocol must be invoked whenever structural re-indexing or bulk migrations have occurred.

## The Rules of Visual Parity
1.  **Direct Vision:** The agent must physically `read_file` every image in the target journal.
2.  **Verbatim Accuracy:** Descriptions must capture the literal content of the image (e.g., specific terminal commands, agent names, file paths shown).
3.  **Semantic Alignment:** The "Key Takeaway" must logically follow from the visual evidence in the screenshot.
4.  **Sequential Correction:** If a mismatch is found, the agent must determine if the image is out of order or if the text is hallucinated, then rectify the journal to restore parity.
5.  **Audit Scrutiny:** Every mismatch found and fixed must be recorded in the session summary.

## Tasks
- [ ] WeDo: AUDIT-01 | Initialize Audit for Target Range
  - ID: AUDIT-01
  - Status: [ ]
  - Description: Define the Year/Quarter/Month/Day range for the audit and locate all `png_journal.md` files.
- [ ] WeDo: AUDIT-02 | Sequential Verification Loop
  - ID: AUDIT-02
  - Status: [ ]
  - Description: For every entry in the target journals, perform a visual-text comparison.
- [ ] WeDo: AUDIT-03 | Final Reconciliation Report
  - ID: AUDIT-03
  - Status: [ ]
  - Description: Summarize the changes made and confirm the current state of parity.
