# Pomodoro Timer

A desktop Pomodoro study/focus timer built with Python's Tkinter. Cycle through focus sessions and breaks using the Pomodoro Technique, with a live animated progress ring and session tracking.

## Features

- 25-minute focus sessions, 5-minute short breaks, and 15-minute long breaks (fully customizable)
- Automatically switches to a **long break** every 4th completed focus session
- Animated circular progress ring that fills as time counts down
- Color-coded phases — red for focus, green for breaks
- Start / Pause, Reset, and Skip controls
- Jump directly to any phase (Focus, Short Break, Long Break) at any time
- Tracks total completed focus sessions
- Auto-advances to the next phase with a bell sound when time runs out
- Clean dark-mode UI, no external dependencies

## Requirements

- Python 3.x
- Tkinter (included with most standard Python installations)

No `pip install` needed — everything used is part of the Python standard library.

## How to Run

```bash
python pomodoro_timer.py
```

On some systems you may need `python3` instead of `python`.

## How to Use

1. Launch the app — it opens in **Focus** mode with 25:00 on the clock.
2. Click **Start** to begin the countdown.
3. Click **Pause** to pause, or **Reset** to restart the current phase.
4. Click **Skip** to jump straight to the next phase.
5. Use the **Jump to** buttons to manually switch between Focus, Short Break, and Long Break at any time.
6. When a focus session finishes, the session counter increases and the app automatically moves to a break (long break every 4th session).

## Customizing

Edit the constants near the top of `pomodoro_timer.py`:

```python
WORK_MINUTES = 25
SHORT_BREAK_MINUTES = 5
LONG_BREAK_MINUTES = 15
SESSIONS_BEFORE_LONG_BREAK = 4
```

Change these values to match your own study/work rhythm.

## File Structure

```
pomodoro_timer.py   # main app — just run this
README.md           # this file
```
