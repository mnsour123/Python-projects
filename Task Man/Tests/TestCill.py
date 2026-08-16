from pathlib import Path

from taskman import cli
from taskman.storage import TaskStore


def run(monkeypatch, tmp_path: Path, args):
    monkeypatch.setattr(cli, "TaskStore", lambda: TaskStore(path=tmp_path / "tasks.json"))
    return cli.main(args)


def test_add_and_list(monkeypatch, tmp_path, capsys):
    assert run(monkeypatch, tmp_path, ["add", "Test task"]) == 0
    assert run(monkeypatch, tmp_path, ["list"]) == 0
    out = capsys.readouterr().out
    assert "Test task" in out


def test_done_marks_complete(monkeypatch, tmp_path, capsys):
    run(monkeypatch, tmp_path, ["add", "Finish me"])
    assert run(monkeypatch, tmp_path, ["done", "1"]) == 0
    out = capsys.readouterr().out
    assert "Completed: Finish me" in out


def test_rm_missing_id_returns_error(monkeypatch, tmp_path, capsys):
    code = run(monkeypatch, tmp_path, ["rm", "42"])
    assert code == 1
    err = capsys.readouterr().err
    assert "No task with id 42" in err