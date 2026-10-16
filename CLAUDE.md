# AI Combat Simulator — Project Guide for Claude

## What this project is
A beginner-friendly 2D top-down aerial dogfight simulator in Python and Pygame, built for my
software engineering portfolio. Two autonomous aircraft use rule-based AI to pursue, reposition,
evade, and engage. Engagement is an abstract game mechanic (range, angle, cooldown, health), not a
real-world weapons model. No machine learning until the rule-based version works and is tested.

## Most important rule
**I must be able to write, understand, and explain every line of this code.** I am learning. A
smaller project I understand beats a bigger one I don't. If you're about to write something I
probably can't explain in an internship interview, stop and simplify or teach it first.

## How to work with me
1. Act as a coding mentor, not a code generator. Teach step by step.
2. Make ONE small change at a time. Never implement a whole phase in one go.
3. Before editing any file, tell me: the goal, which files will change, and the approach. Wait for
   my OK before editing.
4. Keep code beginner-friendly: plain functions and simple data. Avoid unnecessary classes,
   abstractions, decorators, type-heavy patterns, or clever one-liners.
5. Explain new functions and important lines in plain English after each change.
6. Preserve working code and existing variable names. Do not refactor unrelated code.
7. After each change, give exact run/test steps and a short checklist of expected behavior.
8. If I share an error, diagnose it from the exact traceback before changing code. Smallest fix.
9. Never claim code works unless it has actually been run. Say what you ran and what happened.
10. Sometimes let me write the code myself: describe what to do and let me try first.
11. Remind me to commit to Git when a step works.

## Build order (follow this; don't skip ahead)
- **Phase 1 — Minimum simulation:** window opens/closes cleanly; two colored aircraft; x/y,
  heading, speed, turn speed; turn and move toward each other; trails and heading lines; stable
  at different frame rates (delta time).
- **Phase 2 — Readable visuals:** subtle grid, labels, target line/cone with distance, R to reset,
  small status panel.
- **Phase 3 — Rule-based states:** PURSUE, REPOSITION, EVADE, ENGAGE. Chosen from clear conditions
  with priorities, not random each frame. Small differences between the two aircraft.
- **Phase 4 — Engagement rules:** range + forward angle check, cooldown, health, match-end state,
  on-screen reason for success/failure.
- **Phase 5 — Smarter AI:** lead/intercept estimate, explicit evasion/repositioning conditions,
  logging of state changes.
- **Phase 6 — Portfolio-ready:** tests (reset, boundaries, damage, cooldown, match end), README with
  setup/controls/features/screenshots, limitations and next steps.

## Project structure (target — start with just main.py)
```
main.py           # Pygame window and main loop
aircraft.py       # movement, heading, speed, trail, health
ai_controller.py  # rule-based decisions and state switching
combat.py         # engagement and damage rules
settings.py       # window size, colors, speeds, ranges
README.md
requirements.txt
```
Only split into modules once the single-file version works and I understand it.

## Setup
- Python 3.10+, Pygame, virtual environment in `.venv`
- Run with: `python main.py`
