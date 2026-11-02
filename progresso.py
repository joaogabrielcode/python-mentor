"""Track exercise completion for the Portuguese or English study path."""

import argparse
from pathlib import Path
import re


ROOT = Path(__file__).resolve().parent
ITEM = re.compile(r"^- \[([ xX])\] \[(.+?)\]\(([^)]+)\)$", re.MULTILINE)
LANGUAGES = {
    "pt": {"readme": "README.md", "progress": "PROGRESSO.md"},
    "en": {"readme": "README.en.md", "progress": "PROGRESS.en.md"},
}
ACTIONS = {
    "status": "status",
    "concluir": "complete",
    "complete": "complete",
    "reabrir": "reopen",
    "reopen": "reopen",
}


def list_exercises(root, language):
    groups = {}
    topic = None
    seen = set()
    readme = root / LANGUAGES[language]["readme"]
    exercise_root = (root / "exercises" / language).resolve()
    for line in readme.read_text(encoding="utf-8").splitlines():
        if line.startswith("## "):
            topic = line[3:]
        elif match := ITEM.fullmatch(line):
            _, title, path = match.groups()
            target = (root / path).resolve()
            if (topic is None or not target.is_relative_to(exercise_root)
                    or not target.is_file() or target.suffix != ".py" or path in seen):
                raise ValueError(f"Invalid exercise in {readme.name}: {path}")
            seen.add(path)
            groups.setdefault(topic, []).append((title, path))
    if not groups:
        raise ValueError(f"No exercises found in {readme.name}.")
    return groups


def read_completed(root, language):
    settings = LANGUAGES[language]
    source = root / settings["progress"]
    if not source.exists():
        source = root / settings["readme"]
    return {
        path for mark, _, path in ITEM.findall(source.read_text(encoding="utf-8"))
        if mark.lower() == "x"
    }


def save_progress(root, language, groups, completed):
    settings = LANGUAGES[language]
    total = sum(len(items) for items in groups.values())
    count = len(completed)
    next_exercise = next(
        ((title, path) for items in groups.values() for title, path in items
         if path not in completed),
        None,
    )
    example_path = next(iter(groups.values()))[0][1]
    if language == "pt":
        summary = f"{count}/{total} exercícios concluídos ({count / total:.1%})."
        current = (f"Exercício atual: [{next_exercise[0]}]({next_exercise[1]})."
                   if next_exercise else "Todos os exercícios foram concluídos.")
        lines = [
            "# Progresso dos exercícios", "", summary, "", current, "",
            "Idioma: português. O progresso em inglês é independente.", "",
            "Após revisar e aprovar sua solução, registre a conclusão:", "", "```sh",
            f"python3 progresso.py concluir {example_path}", "```", "",
            "Use `reabrir` no lugar de `concluir` para voltar a pendente.",
            "Execute `python3 progresso.py` para sincronizar os totais.",
            "O registro não verifica soluções, não atribui notas nem cria commits.", "",
            "| Assunto | Concluídos | Progresso |", "| --- | --- | --- |",
        ]
    else:
        summary = f"{count}/{total} exercises completed ({count / total:.1%})."
        current = (f"Current exercise: [{next_exercise[0]}]({next_exercise[1]})."
                   if next_exercise else "All exercises have been completed.")
        lines = [
            "# Exercise progress", "", summary, "", current, "",
            "Language: English. Portuguese progress is tracked separately.", "",
            "After reviewing and approving your solution, record completion:", "", "```sh",
            f"python3 progresso.py --language en complete {example_path}", "```", "",
            "Use `reopen` instead of `complete` to mark an exercise as pending.",
            "Run `python3 progresso.py --language en` to synchronize totals.",
            "This record does not check solutions, assign scores or create commits.", "",
            "| Topic | Completed | Progress |", "| --- | --- | --- |",
        ]
    for topic, items in groups.items():
        done = sum(path in completed for _, path in items)
        lines.append(f"| {topic} | {done}/{len(items)} | {done / len(items):.0%} |")
    for topic, items in groups.items():
        lines.extend(["", f"## {topic}", ""])
        for title, path in items:
            mark = "x" if path in completed else " "
            lines.append(f"- [{mark}] [{title}]({path})")
    (root / settings["progress"]).write_text("\n".join(lines) + "\n", encoding="utf-8")

    def synchronize(match):
        _, title, path = match.groups()
        mark = "x" if path in completed else " "
        return f"- [{mark}] [{title}]({path})"

    readme = root / settings["readme"]
    original = readme.read_text(encoding="utf-8")
    updated = ITEM.sub(synchronize, original)
    if original != updated:
        readme.write_text(updated, encoding="utf-8")
    return summary


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--language", choices=LANGUAGES,
                        help="Study language; defaults to pt or follows the exercise path.")
    parser.add_argument("action", nargs="?", default="status", choices=ACTIONS)
    parser.add_argument("exercise", nargs="?", help="Exercise .py path relative to the project root.")
    args = parser.parse_args()
    action = ACTIONS[args.action]
    if action != "status" and not args.exercise:
        parser.error("Specify an exercise path for complete/concluir or reopen/reabrir.")
    if action == "status" and args.exercise:
        parser.error("The status action does not take an exercise path.")
    try:
        path = None
        if args.exercise:
            target = Path(args.exercise)
            if not target.is_absolute():
                target = ROOT / target
            path = target.resolve().relative_to(ROOT).as_posix()
        language = args.language
        if language is None:
            language = "en" if path and path.startswith("exercises/en/") else "pt"
        groups = list_exercises(ROOT, language)
        paths = {path for items in groups.values() for _, path in items}
        completed = read_completed(ROOT, language) & paths
        if path is not None:
            if path not in paths:
                raise ValueError(f"Exercise is not in the {language} checklist: {path}")
            if action == "complete":
                completed.add(path)
            else:
                completed.discard(path)
        print(save_progress(ROOT, language, groups, completed))
    except (OSError, ValueError) as error:
        parser.exit(1, f"Could not update progress: {error}\n")


if __name__ == "__main__":
    main()
