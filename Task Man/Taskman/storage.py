"""JSON-backed storage for tasks."""
from __future__ import annotations

import json
from dataclasses import asdict, dataclass, field
from datetime import datetime
from pathlib import Path
from typing import List, Optional

DEFAULT_DB_PATH = Path.home() / ".taskman" / "tasks.json"


@dataclass
class Task:
    id: int
    title: str
    done: bool = False
    priority: str = "normal"  # low | normal | high
    created_at: str = field(default_factory=lambda: datetime.now().isoformat(timespec="seconds"))
    completed_at: Optional[str] = None

    def to_dict(self) -> dict:
        return asdict(self)

    @classmethod
    def from_dict(cls, data: dict) -> "Task":
        return cls(**data)


class TaskStore:
    """Loads and saves a list of tasks to a JSON file."""

    def __init__(self, path: Path = DEFAULT_DB_PATH):
        self.path = Path(path)
        self.tasks: List[Task] = []
        self._load()

    def _load(self) -> None:
        if self.path.exists():
            raw = json.loads(self.path.read_text())
            self.tasks = [Task.from_dict(t) for t in raw]
        else:
            self.tasks = []

    def save(self) -> None:
        self.path.parent.mkdir(parents=True, exist_ok=True)
        self.path.write_text(json.dumps([t.to_dict() for t in self.tasks], indent=2))

    def _next_id(self) -> int:
        return max((t.id for t in self.tasks), default=0) + 1

    def add(self, title: str, priority: str = "normal") -> Task:
        task = Task(id=self._next_id(), title=title, priority=priority)
        self.tasks.append(task)
        self.save()
        return task

    def complete(self, task_id: int) -> Task:
        task = self.get(task_id)
        task.done = True
        task.completed_at = datetime.now().isoformat(timespec="seconds")
        self.save()
        return task

    def remove(self, task_id: int) -> Task:
        task = self.get(task_id)
        self.tasks.remove(task)
        self.save()
        return task

    def get(self, task_id: int) -> Task:
        for t in self.tasks:
            if t.id == task_id:
                return t
        raise KeyError(f"No task with id {task_id}")

    def list(self, show_done: bool = False) -> List[Task]:
        if show_done:
            return list(self.tasks)
        return [t for t in self.tasks if not t.done]