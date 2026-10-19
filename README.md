# AI FightClub

A 2D top-down dogfight simulator written in Python with Pygame. Two jets fly on their own,
turning toward and chasing each other. There is no player control: the goal is to build
readable, rule-based AI step by step, then add engagement rules, smarter decisions and tests.

> **Status:** work in progress. Phase 1 (core flight simulation) is complete. See the
> [roadmap](#roadmap) for what's next.

## What it does right now

- Opens fullscreen at your screen's size, over a desert map
- Two jets, an F-18 and a Su-27, each with its own position, heading, speed and turn speed
- Each jet aims at the other and turns toward it smoothly, limited by its turn speed and
  always turning the shorter way around
- A trail behind each jet shows its last ~2 seconds of flight
- An aim line sticks out of each jet's nose to show where it is pointing
- Movement is frame-rate independent: speeds are in pixels per second and turn speeds in
  degrees per second, scaled by the time between frames (delta time)

## Setup

Requires **Python 3.10+**.

```bash
# 1. Create a virtual environment (once)
python3 -m venv .venv

# 2. Activate it (every new terminal)
source .venv/bin/activate        # macOS / Linux
.venv\Scripts\activate           # Windows

# 3. Install Pygame (once)
pip install pygame
```

## Run

From the project folder, with the virtual environment active:

```bash
python main.py
```

## Controls

| Key | Action |
|-----|--------|
| Esc | Quit |

The jets fly themselves; there is nothing else to control yet.

## How it works

Everything runs in one loop in `main.py`, once per frame:

1. **Time step:** `clock.tick(60)` caps the game at 60 FPS and returns how long the last frame
   took. Every movement is multiplied by this `dt`, so the jets move at the same speed on
   fast and slow computers.
2. **Aim:** each jet finds the direction to its opponent with `atan2(dy, dx)`.
3. **Turn:** `turnTowards()` compares the current heading with that target, picks the shorter
   way around the circle, and turns by at most `turnSpeed × dt` degrees.
4. **Move:** the heading is split into x and y parts with `cos` and `sin`, then scaled by
   `speed × dt`.
5. **Draw:** background, trails, aim lines, then the jets, each rotated to match its heading
   and centered on its position.

Each jet's state is stored in a dictionary (`x`, `y`, `heading`, `speed`, `turningSpeed`).

**Heading convention:** 0° = right, 90° = down, 180° = left, 270° = up (Pygame's y-axis
points down).

## Project structure

```
main.py      # window, game loop, jet logic and drawing
img/         # jet sprites and map backgrounds
```

The plan is to split `main.py` into `aircraft.py`, `ai_controller.py`, `combat.py` and
`settings.py` as the project grows.

## Roadmap

- [x] **Phase 1: Core simulation.** Window, two jets, heading/speed/turning, chasing, trails,
      aim lines, delta time
- [ ] **Phase 2: Readable visuals.** Grid, labels, target line with distance, R to reset,
      status panel
- [ ] **Phase 3: Rule-based states.** PURSUE, REPOSITION, EVADE and ENGAGE, chosen by clear,
      prioritized conditions; small differences between the two jets
- [ ] **Phase 4: Engagement rules.** Range and forward-angle checks, cooldown, health, match
      end with an on-screen reason
- [ ] **Phase 5: Smarter AI.** Lead/intercept estimates, explicit evade/reposition
      conditions, logging of state changes
- [ ] **Phase 6: Portfolio-ready.** Tests (reset, boundaries, damage, cooldown, match end),
      screenshots, limitations and next steps

Engagement is an abstract game mechanic (range, angle, cooldown, health), not a model of real
weapons.

## Credits

Jet sprites, map backgrounds and the menu image in `img/` were generated with ChatGPT.

## Known limitations

- Jets can fly off the edge of the screen; there are no boundaries yet
- Both jets use the same simple pursuit logic, so they often end up circling each other
- The map image is stretched to fit the screen, so it may look slightly distorted on some
  screen shapes
