"""Работа с отметками учебника (не с решениями практических работ)."""
from __future__ import annotations

import json
from pathlib import Path
from typing import Iterable

DEFAULT_PROGRESS_FILE = Path.home() / ".flet_academy" / "course_progress.json"


def empty_progress() -> dict[str, set[str]]:
    return {"quiz": set(), "done": set()}


def load_progress(
    path: Path = DEFAULT_PROGRESS_FILE,
    valid_slugs: Iterable[str] | None = None,
) -> dict[str, set[str]]:
    """Читает сохранённый прогресс; повреждённый файл не ломает учебник."""
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, ValueError, TypeError):
        return empty_progress()
    if not isinstance(data, dict):
        return empty_progress()

    allowed = set(valid_slugs) if valid_slugs is not None else None
    result = empty_progress()
    for key in result:
        values = data.get(key, [])
        if not isinstance(values, list):
            continue
        result[key] = {
            slug for slug in values
            if isinstance(slug, str) and (allowed is None or slug in allowed)
        }
    return result


def save_progress(state: dict[str, set[str]], path: Path = DEFAULT_PROGRESS_FILE) -> None:
    """Атомарно сохраняет обе независимые отметки: тест и практику."""
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_name(path.name + ".tmp")
    temporary.write_text(
        json.dumps({key: sorted(state[key]) for key in ("quiz", "done")},
                   ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    temporary.replace(path)


def reset_lesson(state: dict[str, set[str]], slug: str) -> None:
    """Сбрасывает только выбранную тему, не удаляя файлы задания."""
    state["quiz"].discard(slug)
    state["done"].discard(slug)


def reset_all(state: dict[str, set[str]]) -> None:
    """Сбрасывает все отметки, не удаляя решения и пользовательские базы."""
    for key in ("quiz", "done"):
        state[key].clear()
