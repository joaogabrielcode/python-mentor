"""Check that one student's language path cannot change another language's progress."""

from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest


SOURCE = Path(__file__).resolve().parents[1]


class ProgressTests(unittest.TestCase):
    def setUp(self):
        self.directory = tempfile.TemporaryDirectory()
        self.addCleanup(self.directory.cleanup)
        self.root = Path(self.directory.name)
        shutil.copy2(SOURCE / 'progresso.py', self.root / 'progresso.py')
        for language, readme in [('pt', 'README.md'), ('en', 'README.en.md')]:
            entries = []
            for number in (1, 2):
                path = f'exercises/{language}/01_variables/ex0{number}.py'
                file = self.root / path
                file.parent.mkdir(parents=True, exist_ok=True)
                file.write_text('# An exercise prompt.\n')
                entries.append(f'- [ ] [{number:02} — Exercise {number}]({path})')
            (self.root / readme).write_text('# Study guide\n\n## Variables\n\n' + '\n'.join(entries) + '\n')
            self.run_cli('--language', language)

    def run_cli(self, *args, succeeds=True):
        result = subprocess.run(
            [sys.executable, '-B', str(self.root / 'progresso.py'), *args],
            text=True, capture_output=True, cwd=self.root,
        )
        self.assertEqual(result.returncode == 0, succeeds, result.stdout + result.stderr)
        return result

    def snapshot(self):
        return {name: (self.root / name).read_bytes() for name in
                ['README.md', 'README.en.md', 'PROGRESSO.md', 'PROGRESS.en.md']}

    def test_default_language_starts_at_zero(self):
        result = self.run_cli()
        self.assertIn('0/2 exercícios concluídos', result.stdout)
        self.assertIn('Current exercise:', (self.root / 'PROGRESS.en.md').read_text())

    def test_english_completion_does_not_change_portuguese(self):
        before = self.snapshot()
        self.run_cli('--language', 'en', 'complete', 'exercises/en/01_variables/ex01.py')
        after = self.snapshot()
        for name in ['README.md', 'PROGRESSO.md']:
            self.assertEqual(before[name], after[name])
        self.assertIn('1/2 exercises completed', after['PROGRESS.en.md'].decode())
        current = after['PROGRESS.en.md'].decode().splitlines()[4]
        self.assertIn('ex02.py', current)

    def test_portuguese_alias_does_not_change_english(self):
        before = self.snapshot()
        self.run_cli('concluir', 'exercises/pt/01_variables/ex01.py')
        after = self.snapshot()
        for name in ['README.en.md', 'PROGRESS.en.md']:
            self.assertEqual(before[name], after[name])
        self.assertIn('1/2 exercícios concluídos', after['PROGRESSO.md'].decode())

    def test_language_is_inferred_from_english_path(self):
        result = self.run_cli('complete', 'exercises/en/01_variables/ex01.py')
        self.assertIn('1/2 exercises completed', result.stdout)

    def test_repeated_completion_and_reopening_are_idempotent(self):
        initial = self.snapshot()
        path = 'exercises/en/01_variables/ex01.py'
        self.run_cli('complete', path)
        completed = self.snapshot()
        self.run_cli('complete', path)
        self.assertEqual(completed, self.snapshot())
        self.run_cli('reopen', path)
        self.assertEqual(initial, self.snapshot())

    def test_wrong_language_and_external_paths_leave_records_unchanged(self):
        initial = self.snapshot()
        self.run_cli('--language', 'pt', 'complete', 'exercises/en/01_variables/ex01.py', succeeds=False)
        self.run_cli('complete', '../outside.py', succeeds=False)
        self.run_cli('complete', 'exercises/pt/01_variables/missing.py', succeeds=False)
        self.assertEqual(initial, self.snapshot())

    def test_new_english_exercise_updates_only_english_total(self):
        readme = self.root / 'README.en.md'
        path = 'exercises/en/01_variables/ex03.py'
        (self.root / path).write_text('# New prompt.\n')
        readme.write_text(readme.read_text() + f'- [ ] [03 — New exercise]({path})\n')
        self.assertIn('0/3 exercises completed', self.run_cli('--language', 'en').stdout)
        self.assertIn('0/2 exercícios concluídos', self.run_cli().stdout)

    def test_checklist_cannot_reference_another_language(self):
        readme = self.root / 'README.en.md'
        readme.write_text(readme.read_text() + '- [ ] [03 — Wrong language](exercises/pt/01_variables/ex01.py)\n')
        before = self.snapshot()
        self.run_cli('--language', 'en', succeeds=False)
        self.assertEqual(before, self.snapshot())


if __name__ == '__main__':
    unittest.main()
