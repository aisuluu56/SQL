"""Техническая проверка комплекта; решения студентов НЕ проверяет."""
import ast
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
LESSONS = json.loads((ROOT/'curriculum.json').read_text(encoding='utf-8'))
assert len(LESSONS) == 28
assert len({i['slug'] for i in LESSONS}) == 28
for item in LESSONS:
    slug = item['slug']
    md = ROOT/'lessons'/f'{slug}.md'
    py = ROOT/'tasks'/f'{slug}.py'
    assert md.is_file() and py.is_file(), slug
    text = md.read_text(encoding='utf-8')
    source = py.read_text(encoding='utf-8')
    assert '## Теория' in text and '## Самостоятельная практика' in text
    assert 'TODO' in source
    ast.parse(source, filename=str(py))
    for part in text.split('```python')[1:]:
        ast.parse(part.split('```')[0], filename=str(md))
    quiz = item['quiz']
    assert len(quiz[1]) == 3 and 0 <= quiz[2] < 3
for code in ('course_app.py', 'course_cli.py', 'check_course.py', 'progress_store.py'):
    ast.parse((ROOT/code).read_text(encoding='utf-8'))
assert (ROOT / 'docker-compose.yml').is_file()
assert (ROOT / '.env.example').is_file()
assert (ROOT / 'db' / 'README.md').is_file()
assert not any((ROOT / 'lessons').glob('*sqlite*'))
assert not any((ROOT / 'tasks').glob('*sqlite*'))
print(f'OK: {len(LESSONS)} тем, столько же заданий, корректный Python-синтаксис.')
print('Графический рендеринг Flet и выполнение заданий не проверялись.')
