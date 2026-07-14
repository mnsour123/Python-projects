# To-Do List App (Tkinter)

A simple, lightweight desktop to-do list application built with Python's built-in `tkinter` GUI library. Tasks are automatically saved to a local JSON file, so your list persists between sessions.

## Features

-  Add new tasks via input box or Enter key
-  Mark tasks as complete/incomplete (double-click)
-  Delete individual tasks
-  Clear all tasks at once (with confirmation)
-  Auto-save/load tasks using `tasks.json`
-  Simple, clean UI with no external dependencies

## Requirements

- Python 3.x
- `tkinter` (comes pre-installed with most Python distributions)

No third-party packages are required.

## Installation

1. Clone or download this repository.
2. Make sure Python 3 is installed on your system:
   ```bash
   python --version
   ```
3. If `tkinter` is not installed (common on some Linux distributions), install it:
   ```bash
   # Debian/Ubuntu
   sudo apt-get install python3-tk

   # Fedora
   sudo dnf install python3-tkinter
   ```

## Usage

Run the app with:

```bash
python todo_app.py
```

### Controls

| Action              | How to do it                          |
|----------------------|----------------------------------------|
| Add a task           | Type in the input box, press **Enter** or click **Add** |
| Mark complete/incomplete | **Double-click** a task in the list |
| Delete a task         | Select it, then click **Delete Selected** |
| Clear all tasks       | Click **Clear All** (confirmation required) |

## Data Storage

Tasks are saved automatically to `tasks.json` in the same directory as the script when you close the app, and are reloaded the next time you open it. The file looks like this:

```json
[
  {"text": "Buy groceries", "done": false},
  {"text": "Finish project report", "done": true}
]
```

## Project Structure

```
.
├── todo_app.py     # Main application file
├── tasks.json      # Auto-generated file storing saved tasks
└── README.md       # This file
```

## Possible Future Enhancements

- Due dates and reminders
- Task priority levels
- Categories/tags for tasks
- Search/filter tasks
- Dark mode theme

## License

This project is free to use and modify for personal or educational purposes.
