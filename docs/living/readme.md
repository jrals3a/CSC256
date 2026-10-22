# docs/living/

This folder contains the **current** agile documents for the TaskTracker project.

These are living documents — they are updated in place every sprint. They always reflect where the project is right now, not where it was in a previous sprint.

---

## What Lives Here

| File | First Created | Purpose |
|------|--------------|---------|
| `sprint_plan.md` | S1_1 | Current sprint goals, scope, and definition of done |
| `architecture.md` | S1_1 | Current application structure and design decisions |
| `test_plan.md` | S1_1 | Current testing strategy, objectives, and tools |
| `test_cases.md` | S1_1 | All test cases — grows every sprint |
| `api_reference.md` | S1_1 | All API endpoints — updated when endpoints change |
| `class_diagram.md` | S3_1 | Current class relationships — added Sprint 3 |
| `erd.md` | S3_1 | Current data model — added Sprint 3 |
| `user_journey.md` | S4_2 | Current user journeys through the UI — added Sprint 4 |

---

## How This Works Across Sprints

### Sprint 1 — Special Case: Created on GitHub.com

The S1_1 Agile Documentation assignment creates all five starter documents directly in this folder **on GitHub.com** — using the web editor. You do not have a local clone yet at this point; the lab that follows S1_1 is where you clone for the first time.

> [!IMPORTANT]
> **S1_1 is the only time you create agile documents on GitHub.com.** From S1_2 onward, all agile document work is done **locally in VS Code**, committed via **GitHub Desktop**, and pushed to GitHub. When you clone the repo at the start of S1_1 Lab, these documents will already be there.

At the end of Sprint 1, `docs/living/` and `docs/checkpoints/s1_1/` contain identical copies — the checkpoint is a snapshot of the S1_1 planning state.

### S1_2 and All Sprints After — Local Workflow, Checkpoint First

From S1_2 onward, all agile document work follows this pattern — done **locally in VS Code**, pushed via **GitHub Desktop**:

```
Sprint _1 assignment (S2_1 onward):
  1. Pull latest main locally (GitHub Desktop → Fetch origin → Pull origin)
  2. Create checkpoint: copy docs/living/* → docs/checkpoints/s#_0/
  3. Update docs/living/ with new sprint planning content in VS Code
  4. Commit via GitHub Desktop → Push → PR → merge
  5. Screenshot the PR Files Changed tab as submission evidence

Sprint _2 assignment:
  1. Pull latest main locally
  2. Create checkpoint: copy docs/living/* → docs/checkpoints/s#_1/
  3. Update docs/living/ to reflect what was actually built in VS Code
  4. Commit via GitHub Desktop → Push → PR → merge
  5. Screenshot the PR Files Changed diff as submission evidence
```

The diff between a checkpoint and the updated living document shows exactly what changed — and that diff is your assignment submission.

---

## Where the History Lives

| Folder | What It Contains |
|--------|-----------------|
| `docs/living/` | Current state — always up to date |
| `docs/checkpoints/s1_1/` | Snapshot after S1_1 planning |
| `docs/checkpoints/s1_2/` | Snapshot after S1_2 updates |
| `docs/checkpoints/s2_1/` | Snapshot after S2_1 planning |
| `docs/checkpoints/s2_2/` | Snapshot after S2_2 updates |
| *(and so on through Sprint 6)* | |

Git history on any file in `docs/living/` also shows every change ever made — with timestamps and commit messages. The checkpoints give you named waypoints; git gives you the full story.

---

## Quick Reference

> All commands below are run in the **VS Code terminal** on your local machine (S1_2 onward). S1_1 is done on GitHub.com — no terminal needed.

**Starting a new sprint (_1 assignment, S2_1 onward):**
```bash
# Pull latest main first
# GitHub Desktop → Fetch origin → Pull origin

# Create checkpoint of prior sprint ending state
mkdir -p docs/checkpoints/s#_0
cp docs/living/* docs/checkpoints/s#_0/

# Then open docs/living/ files in VS Code and update with new sprint content
# Commit via GitHub Desktop → Push → PR → merge
```

**Updating after a lab (_2 assignment):**
```bash
# Pull latest main first
# GitHub Desktop → Fetch origin → Pull origin

# Create checkpoint of current sprint planning state
mkdir -p docs/checkpoints/s#_1
cp docs/living/* docs/checkpoints/s#_1/

# Then open docs/living/ files in VS Code and update to reflect actual implementation
# Commit via GitHub Desktop → Push → PR → merge
```

**Full explanation:** See `REFERENCE_Living_Agile_Documents.md` on Blackboard (Supplemental Materials → Reference).
