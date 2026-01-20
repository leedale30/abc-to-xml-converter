# Antigravity Project Rules

## Agentic Skills Setup

- This project uses a global library of agentic skills.
- The master library is stored at `~/antigravity-skills`.
- To enable these skills in any new project, create the `.agent` directory and symlink the master library:

  ```bash
  mkdir -p .agent && ln -s ~/antigravity-skills .agent/skills
  ```

## Development Standards

- Always refer to relevant skills in `~/antigravity-skills` (linked via `.agent/skills`) for domain-specific expertise.
- Follow the guidelines in `senior-fullstack` and `javascript-mastery` for all code changes.
