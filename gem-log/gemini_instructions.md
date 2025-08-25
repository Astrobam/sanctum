# Gemini Operating Instructions for Project Sanctum

This document outlines the specific workflow and rules to follow for all interactions related to Project Sanctum. Refer to these instructions at the beginning of every new chat session to ensure consistency.

---
## 1. Session & Log Management

- **Start of Session:** At the beginning of a new project session, immediately create a new session log file using the `touch` command. The naming convention is `gem-log/Session-[YYYY-MM-DD]-[Number].md`.
- **End of Session:** At the end of a session, provide a summary of all tasks completed within that session. This summary should be formatted as markdown, ready to be pasted into the current session log file.

---
## 2. File Management

- **File Creation:** Before providing the content for any new file, **always** provide the complete terminal command(s) to create it first (e.g., `mkdir -p docs/diagram`, `touch docs/diagram/filename.md`).
- **File Content:** Always provide the **full, complete content** for any new or updated file. Do not provide partial snippets or diffs.
- **Delivery Format:** All documents, code, and file content must be delivered in markdown format, enclosed within a markdown code block (```).

---
## 3. Project & Git Workflow

- **New Project Kick-off:**
    1.  Begin by asking for the user's development environment (`uname`, `python --version`, etc.).
    2.  Start by creating foundational files like `.gitignore` and any version management files (e.g., `.python-version`).
    3.  The project objective should be captured in `gem-log/intro.md`.
- **Committing Work:** At the end of a session, after providing the session log summary, provide the complete `git add` and `git commit -m "..."` commands to save the work. The commit message should follow conventional commit standards (e.g., `docs:`, `feat:`, `fix:`).

---
## 4. Content & Code Quality

- **Verification:** Avoid a trial-and-error approach. Think carefully about each step and verify your responses to ensure they are correct and address the user's requirements accurately.
- **Clarity & Conciseness:** Keep responses concise and to the point. Avoid unnecessary conversational filler.
- **Diagrams (Mermaid):**
    - All diagrams must be placed in the `docs/diagram/` directory.
    - Diagram files must have a `.md` extension.
    - The filename should be descriptive and **not** include the prefix `diagram_`.
    - The content of these files must be valid Mermaid code, wrapped in a `mermaid` fenced code block.
    - Do **not** use parentheses `()` inside of HTML-like tags (e.g., `<br/><i>...</i>`) within Mermaid labels.
