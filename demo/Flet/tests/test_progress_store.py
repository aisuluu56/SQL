"""Запуск из корня курса: python -m unittest discover -s tests -v"""
import json
import tempfile
import unittest
from pathlib import Path

from progress_store import empty_progress, load_progress, reset_all, reset_lesson, save_progress


class ProgressTests(unittest.TestCase):
    def test_reset_one_keeps_another(self):
        state = {"quiz": {"01_start", "02_text_icons"}, "done": {"01_start", "02_text_icons"}}
        reset_lesson(state, "01_start")
        self.assertEqual(state, {"quiz": {"02_text_icons"}, "done": {"02_text_icons"}})
        reset_lesson(state, "01_start")  # повторный сброс безопасен

    def test_reset_all_and_persist(self):
        with tempfile.TemporaryDirectory() as directory:
            file = Path(directory) / "nested" / "progress.json"
            state = {"quiz": {"01_start"}, "done": {"01_start"}}
            save_progress(state, file)
            self.assertEqual(load_progress(file), state)
            reset_all(state)
            save_progress(state, file)
            self.assertEqual(load_progress(file), empty_progress())

    def test_damaged_file_and_unknown_slugs(self):
        with tempfile.TemporaryDirectory() as directory:
            file = Path(directory) / "progress.json"
            file.write_text('not JSON', encoding="utf-8")
            self.assertEqual(load_progress(file), empty_progress())
            file.write_text(json.dumps({"quiz": ["01_start", "unknown"], "done": ["unknown"]}), encoding="utf-8")
            self.assertEqual(load_progress(file, ["01_start"]), {"quiz": {"01_start"}, "done": set()})


if __name__ == "__main__":
    unittest.main()
