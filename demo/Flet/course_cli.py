"""Текстовый навигатор по урокам: python course_cli.py."""
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
LESSONS = json.loads((ROOT/'curriculum.json').read_text(encoding='utf-8'))

def main():
    while True:
        print('\n=== Flet Academy ===')
        for i, lesson in enumerate(LESSONS, 1):
            print(f'{i:02d}. {lesson["title"]}')
        choice = input('Номер урока (0 — выход): ').strip()
        if choice == '0':
            return
        if not choice.isdigit() or not 1 <= int(choice) <= len(LESSONS):
            print('Некорректный номер.')
            continue
        item = LESSONS[int(choice)-1]
        note = ROOT/'lessons'/f'{item["slug"]}.md'
        task = ROOT/'tasks'/f'{item["slug"]}.py'
        print(f'Теория: {note}\nЗадание: {task}\nЦель: {item["goal"]}')
        if input('Запустить задание? [д/н]: ').lower() in ('д', 'да', 'y', 'yes'):
            subprocess.run([sys.executable, str(task)], cwd=ROOT, check=False)

if __name__ == '__main__':
    main()
