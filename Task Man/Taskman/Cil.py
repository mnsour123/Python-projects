"""Command-line interface for taskman."""
from __future__ import annotations

import argparse
import sys

from .storage import TaskStore, Task

PRIORITY_MARK = {"low": "↓", "normal": "-", "high": "!"}


def format_task(t: Task) -> str:
    box = "[x]" if t.done else "[ ]"
    mark = PRIORITY_MARK.get(t.priority, "-")
    return f"{t.id:>3} {box} {mark} {t.title}"


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="taskman", description="A tiny command-line task manager.")
    sub = parser.add_subparsers(dest="command", required=True)

    p_add = sub.add_parser("add", help="Add a new task")
    p_add.add_argument("title", help="Task description")
    p_add.add_argument("-p", "--priority", choices=["low", "normal", "high"], default="normal")

    p_list = sub.add_parser("list", help="List tasks")
    p_list.add_argument("-a", "--all", action="store_true", help="Include completed tasks")

    p_done = sub.add_parser("done", help="Mark a task as complete")
    p_done.add_argument("id", type=int)

    p_rm = sub.add_parser("rm", help="Remove a task")
    p_rm.add_argument("id", type=int)

    return parser


def main(argv=None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    store = TaskStore()

    try:
        if args.command == "add":
            task = store.add(args.title, args.priority)
            print(f"Added task {task.id}: {task.title}")

        elif args.command == "list":
            tasks = store.list(show_done=args.all)
            if not tasks:
                print("No tasks. Add one with: taskman add \"Do something\"")
            for t in tasks:
                print(format_task(t))

        elif args.command == "done":
            task = store.complete(args.id)
            print(f"Completed: {task.title}")

        elif args.command == "rm":
            task = store.remove(args.id)
            print(f"Removed: {task.title}")

    except KeyError as e:
        print(f"Error: {e}", file=sys.stderr)
        return 1

    return 0


if __name__ == "__main__":
    sys.exit(main())