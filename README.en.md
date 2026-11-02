# Python Mentor

[Português](README.md) | English

I created Python Mentor to learn Python from scratch through exercises, with AI
as a study mentor. My goal is to build a foundation in the language and learn
to solve problems on my own before studying Django as my first Python web
framework.

The exercises cover situations such as calculating commissions, updating
inventory and organizing customer data. This repository keeps my attempts,
solutions and learning history. I will add more exercises as my studies progress.

## Learning path

The topics follow this order:

| Directory | What to practice |
| --- | --- |
| [01_variables](01_variables/) | Variables, arithmetic, percentages and comparisons |
| [02_strings](02_strings/) | Formatting, string methods and slicing |
| [03_inputs](03_inputs/) | User input and type conversion |
| [04_lists](04_lists/) | Indices, updates, sorting and calculations with lists |
| [05_conditionals](05_conditionals/) | Decisions with `if`, `elif`, `else` and logical operators |
| [06_dictionaries](06_dictionaries/) | Keys, values, lookups and data updates |
| [07_for_loops](07_for_loops/) | Iteration, filtering and accumulators |
| [08_functions](08_functions/) | Parameters, return values and code reuse |
| [09_tuples](09_tuples/) | Tuples, unpacking and returning multiple values |

Directory names and section headings are in English. Exercise prompts,
exercise filenames and study records are in Portuguese. Some files contain
only a prompt, ready for a future study session.

## Choosing a branch

This repository has two versions:

| Branch | Contents |
| --- | --- |
| `main` | All exercise prompts, space for solutions and progress set to zero |
| `my-practice` | My solutions, reviews and personal progress |

To start from scratch, visit the [main branch](https://github.com/joaogabrielcode/python-mentor/tree/main).
It contains `exercises/pt/` and `exercises/en/`, with prompts and progress
tracked separately for each language. Follow that branch's guide to clone the
starter version or download its ZIP. The command below clones my practice version.
My personal solutions remain public on `my-practice`.

To save and publish your own progress, fork the repository and use your fork's
URL when cloning. After cloning, create your own study branch:

```sh
git switch -c my-study
```

To follow my solutions, visit the
[my-practice branch](https://github.com/joaogabrielcode/python-mentor/tree/my-practice).
This branch keeps my Portuguese exercises in the numbered root directories,
with its own checklist and review history.

## Getting started

You need Python 3, Git to clone the repository, a text or code editor and a
terminal. The current exercises
use Python's built-in features and require no external libraries.

Clone the repository and enter its directory:

```sh
git clone --single-branch --branch my-practice https://github.com/joaogabrielcode/python-mentor.git
cd python-mentor
```

Check that Python is available:

```sh
python3 --version
```

If your Python 3 installation uses the `python` command, replace `python3` with
`python` in the examples below.

## Running an exercise

Open a file and read its opening comments for the prompt and required data.
Write your attempt below `# Sua solução:` (your solution). Then run the file
from the project root:

```sh
python3 01_variables/ex01_bonus_vendas.py
```

Exercises that use `input` wait for you to type data in the terminal. To
practice entering values, for example:

```sh
python3 03_inputs/ex03_faturamento_lojas.py
```

Follow the format specified in the prompt. This exercise expects a decimal
point, as in `1500.50`. Other exercises specifically handle decimal commas
and currency symbols.

Compare the output with the result you calculated before running the program.
If an error appears, read the indicated line and try to understand its cause
before changing the code.

## Using AI as a mentor

You can study with Codex, Claude or another AI tool that can receive the project
instructions and context. The AI's role is to explain concepts, help break
problems into steps and review your attempts.

### Load the mentoring instructions

[AGENTS.md](AGENTS.md) contains the study rules. The
[python-mentor](.agents/skills/python-mentor/SKILL.md) skill describes
beginner-level reviews, gradual hints and learning records.

In a tool with file access, open the project directory and ask it to read these
documents before starting. How instructions and skills are loaded depends on
the tool. In a chat without repository access, paste or attach both documents,
the exercise prompt and your attempt.

You can start a session with:

```text
I want to study Python with you as my mentor.
Read AGENTS.md and .agents/skills/python-mentor/SKILL.md.
Check PROGRESSO.md and PROGRESSO_PYTHON.md to find where I left off.
Use beginner-level explanations and gradual hints.
Let me try solving the exercise before showing a complete solution.
Ask for my permission before editing an exercise.
```

If the AI cannot access a file, provide its contents. Reviewing an attempt
requires both the exercise prompt and your current code. The mentoring
instructions are written in Portuguese; you can request explanations in English.

### Ask for help while solving

Make your own attempt first. When you get stuck, share the relevant code and
explain which part of the reasoning is unclear. For example:

```text
I don't understand when to use floor division and modulo.
Explain with an example different from the exercise, then give me a hint
so I can try to continue on my own.
```

You can also ask the AI to explain an error message or help choose inputs to
check your result. Under this project's mentoring rules, complete solutions
are provided when explicitly requested.

### Request a review

After running your attempt, ask for a review and specify the file:

```text
I finished 08_functions/ex01_padronizar_produtos.py.
Review my code following the python-mentor skill.
```

The review checks the prompt and logic and runs the solution when possible.
It gives a result, a score from 0 to 10, what works and what needs improvement.
If corrections are required, make another attempt and request another review.
The history is kept in [PROGRESSO_PYTHON.md](PROGRESSO_PYTHON.md).

Saying you finished requests a review. After approval, the AI asks whether you
want to mark the exercise as complete and explains that this includes a commit
and push. Confirming authorizes that workflow for the approved exercise.
Directly asking to mark an approved exercise as complete also authorizes it.

An AI with chat access alone can explain concepts and review what you share.
Editing records or running Git requires access to the files and commands;
otherwise, you carry out those steps yourself.

## Tracking progress

| File | Purpose |
| --- | --- |
| [README.md](README.md) | Portuguese guide and exercise checklist |
| [README.en.md](README.en.md) | English version of the guide |
| [PROGRESSO.md](PROGRESSO.md) | Completion summary and next pending exercise |
| [PROGRESSO_PYTHON.md](PROGRESSO_PYTHON.md) | Reviews, difficulties and resume notes |
| [progresso.py](progresso.py) | Updates to the checklist and totals |

Both guides share the [checklist in the Portuguese README](README.md#variables).
On `main`, the checklist starts at zero. On `my-practice`, the records reflect
my personal progress. On your own study branch, you track your own solutions
and reviews. The progress records are in Portuguese.

To synchronize totals without completing another exercise:

```sh
python3 progresso.py
```

Once a solution has been reviewed and approved, record its completion. For
example, use this command for product standardization only after it is approved:

```sh
python3 progresso.py concluir 08_functions/ex01_padronizar_produtos.py
```

To mark that exercise as pending again:

```sh
python3 progresso.py reabrir 08_functions/ex01_padronizar_produtos.py
```

The command names are Portuguese: `concluir` means complete and `reabrir` means
reopen. The script updates `README.md` and `PROGRESSO.md`. It does not run the
solution, assign a score or create commits. In the AI mentoring workflow, the
review history is updated separately according to the mentoring instructions.

Commits use English and describe the implemented behavior, such as
`feat(variables): calculate sales bonuses and remaining revenue`.
For files that contain only a prompt, the commit identifies the prompt addition.

## Adding exercises

I will expand this repository with new problems as I learn more concepts.
To add an exercise, create a `.py` file in the topic directory, write the prompt
in comments and add an entry to the corresponding checklist section. For a new
topic, also create a numbered directory and a checklist section with a `##`
heading.

After adding the entry, run `python3 progresso.py` to update the totals. The
script reads the exercises from the checklist and verifies that the referenced
files exist. The next study step remains the first pending exercise in checklist
order.
