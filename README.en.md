# Python Mentor

[Português](README.md) | English

Python Mentor is a project for learning Python from scratch through exercises
and AI mentoring. Its goal is to develop programming logic and a foundation in
the language before studying Django as a first Python web framework.

The exercises cover situations such as calculating commissions, updating
inventory and organizing customer data. This branch contains prompts and space
for your own attempts. I will add more exercises as my studies progress.

## Learning path

The topics follow this order:

| Directory | What to practice |
| --- | --- |
| [01_variables](exercises/en/01_variables/) | Variables, arithmetic, percentages and comparisons |
| [02_strings](exercises/en/02_strings/) | Formatting, string methods and slicing |
| [03_inputs](exercises/en/03_inputs/) | User input and type conversion |
| [04_lists](exercises/en/04_lists/) | Indices, updates, sorting and calculations with lists |
| [05_conditionals](exercises/en/05_conditionals/) | Decisions with `if`, `elif`, `else` and logical operators |
| [06_dictionaries](exercises/en/06_dictionaries/) | Keys, values, lookups and data updates |
| [07_for_loops](exercises/en/07_for_loops/) | Iteration, filtering and accumulators |
| [08_functions](exercises/en/08_functions/) | Parameters, return values and code reuse |
| [09_tuples](exercises/en/09_tuples/) | Tuples, unpacking and returning multiple values |

Directory names and section headings are in English. Under `exercises/en/`,
prompts, filenames and study records are in English. The matching Portuguese
exercises are under `exercises/pt/`. All exercise files start without solutions.

## Choosing a branch

| Branch | Contents |
| --- | --- |
| `main` | Blank Portuguese and English exercises for learning from scratch |
| `my-practice` | My Portuguese solutions and personal study progress |

This is the starter version. Choose your language:

- [English exercises](exercises/en/): 43 prompts, with a checklist in this README.
- [Português](README.md): 43 prompts in `exercises/pt/`, with a Portuguese guide and checklist.

The matching exercises practice the same concepts. Each language has its own
progress records; you only need to study the version you prefer. English prompts
translate instructions, required function names and output messages. Proper names
and some sample data are preserved and explained where needed.

The clone below downloads only the current `main` snapshot, without the history
containing answers. You can also download the ZIP for `main` from GitHub.
Personal solutions remain public on the
[my-practice branch](https://github.com/joaogabrielcode/python-mentor/tree/my-practice).

To publish your own progress, fork the repository and use your fork's URL when
cloning. After cloning, create a study branch before solving exercises:

```sh
git switch -c my-study
```

## Getting started

You need Python 3, Git to clone the repository, a text or code editor and a
terminal. The current exercises use Python's built-in features and require no external libraries.

Clone the repository and enter its directory:

```sh
git clone --depth 1 --single-branch --branch main https://github.com/joaogabrielcode/python-mentor.git
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
The starter files contain comments only; running them before writing a solution
produces no output. Write your attempt below `# Your solution:`, then run the file
from the project root:

```sh
python3 exercises/en/01_variables/ex01_sales_bonus.py
```

Exercises that use `input` wait for you to type data in the terminal. To
practice entering values, for example:

```sh
python3 exercises/en/03_inputs/ex03_store_revenue.py
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
I want to study the English version under exercises/en/.
Check PROGRESS.en.md and MENTORING.en.md to find where I left off.
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
I finished exercises/en/01_variables/ex01_sales_bonus.py.
Review my code following the python-mentor skill.
```

The review checks the prompt and logic and runs the solution when possible.
It gives a result, a score from 0 to 10, what works and what needs improvement.
If corrections are required, make another attempt and request another review.
The history is kept in [MENTORING.en.md](MENTORING.en.md).

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
| [README.md](README.md) | Portuguese guide and checklist |
| [README.en.md](README.en.md) | English guide and checklist |
| [PROGRESS.en.md](PROGRESS.en.md) | Completion summary and next pending exercise |
| [MENTORING.en.md](MENTORING.en.md) | Reviews, difficulties and resume notes |
| [progresso.py](progresso.py) | Updates to the checklist and totals |

The checklist below tracks only the English exercises. The
[Portuguese README](README.md) has a separate checklist. Both start at 0/43,
with no previous reviews. Save your attempts on your own study branch.

To synchronize totals without completing another exercise:

```sh
python3 progresso.py --language en
```

Once a solution has been reviewed and approved, record its completion. For
example, use this command for the sales bonus exercise only after it is approved:

```sh
python3 progresso.py --language en complete exercises/en/01_variables/ex01_sales_bonus.py
```

To mark that exercise as pending again:

```sh
python3 progresso.py --language en reopen exercises/en/01_variables/ex01_sales_bonus.py
```

Use `--language en` to select the English records. The commands `complete`
and `reopen` update `README.en.md` and `PROGRESS.en.md`. It does not run the
solution, assign a score or create commits. In the AI mentoring workflow, the
review history is updated separately according to the mentoring instructions.

Commits use English and describe the implemented behavior, such as
`feat(variables): calculate sales bonuses and remaining revenue`.
For files that contain only a prompt, the commit identifies the prompt addition.

## Adding exercises

I will expand this repository with new problems as I learn more concepts.
To add an exercise, create matching `.py` files in the topic directories under
`exercises/pt/` and `exercises/en/`, write the prompts in comments and add each
entry to its language's README checklist. For a new topic, also create a numbered directory and a checklist section with a `##`
heading.

After adding entries, run `python3 progresso.py` and
`python3 progresso.py --language en` to update totals for both languages. The
script reads the exercises from the checklist and verifies that the referenced
files exist. The next study step is the first pending exercise in the selected language's
checklist order.

## Variables

- [ ] [01 — Sales bonus](exercises/en/01_variables/ex01_sales_bonus.py)
- [ ] [02 — Inventory balance](exercises/en/01_variables/ex02_inventory_balance.py)
- [ ] [03 — Cargo distribution](exercises/en/01_variables/ex03_cargo_distribution.py)
- [ ] [04 — Profit margin](exercises/en/01_variables/ex04_profit_margin.py)
- [ ] [05 — Contract duration](exercises/en/01_variables/ex05_contract_duration.py)

## Strings

- [ ] [01 — Profit report](exercises/en/02_strings/ex01_profit_report.py)
- [ ] [02 — Customer data normalization](exercises/en/02_strings/ex02_normalize_customer.py)
- [ ] [03 — Email domain replacement](exercises/en/02_strings/ex03_replace_domain.py)
- [ ] [04 — Username extraction](exercises/en/02_strings/ex04_extract_username.py)
- [ ] [05 — Customer greeting](exercises/en/02_strings/ex05_customer_greeting.py)

## User input

- [ ] [01 — Sales tax](exercises/en/03_inputs/ex01_sales_tax.py)
- [ ] [02 — Employee registration](exercises/en/03_inputs/ex02_employee_registration.py)
- [ ] [03 — Store revenue](exercises/en/03_inputs/ex03_store_revenue.py)

## Lists

- [ ] [01 — Sales report](exercises/en/04_lists/ex01_sales_report.py)
- [ ] [02 — Inventory editing](exercises/en/04_lists/ex02_edit_inventory.py)
- [ ] [03 — Shipping cost sorting](exercises/en/04_lists/ex03_sort_shipping_costs.py)
- [ ] [04 — Delivery route](exercises/en/04_lists/ex04_delivery_route.py)
- [ ] [05 — Price updates](exercises/en/04_lists/ex05_update_prices.py)

## Conditionals

- [ ] [01 — Investment profile](exercises/en/05_conditionals/ex01_investment_profile.py)
- [ ] [02 — System access](exercises/en/05_conditionals/ex02_system_access.py)
- [ ] [03 — Progressive discount](exercises/en/05_conditionals/ex03_progressive_discount.py)
- [ ] [04 — Target-based bonus](exercises/en/05_conditionals/ex04_target_bonus.py)
- [ ] [05 — Email routing](exercises/en/05_conditionals/ex05_route_emails.py)

## Dictionaries

- [ ] [01 — Customer updates](exercises/en/06_dictionaries/ex01_update_customers.py)
- [ ] [02 — Inventory lookup](exercises/en/06_dictionaries/ex02_lookup_inventory.py)
- [ ] [03 — Regional revenue](exercises/en/06_dictionaries/ex03_regional_revenue.py)
- [ ] [04 — Average performance](exercises/en/06_dictionaries/ex04_average_performance.py)
- [ ] [05 — Product removal](exercises/en/06_dictionaries/ex05_remove_product.py)

## For loops

- [ ] [01 — Training reminders](exercises/en/07_for_loops/ex01_training_reminders.py)
- [ ] [02 — Sales commission](exercises/en/07_for_loops/ex02_sales_commission.py)
- [ ] [03 — Critical stock](exercises/en/07_for_loops/ex03_critical_stock.py)
- [ ] [04 — Monthly costs](exercises/en/07_for_loops/ex04_monthly_costs.py)
- [ ] [05 — Price adjustment](exercises/en/07_for_loops/ex05_adjust_prices.py)

## Functions

- [ ] [01 — Product standardization](exercises/en/08_functions/ex01_standardize_products.py)
- [ ] [02 — ISS calculation](exercises/en/08_functions/ex02_calculate_iss.py)
- [ ] [03 — Margin analysis](exercises/en/08_functions/ex03_analyze_margin.py)
- [ ] [04 — Target checks](exercises/en/08_functions/ex04_check_targets.py)
- [ ] [05 — Currency conversion](exercises/en/08_functions/ex05_convert_currency.py)

## Tuples

- [ ] [01 — Delivery coordinates](exercises/en/09_tuples/ex01_delivery_coordinates.py)
- [ ] [02 — Payroll](exercises/en/09_tuples/ex02_payroll.py)
- [ ] [03 — Product sales](exercises/en/09_tuples/ex03_product_sales.py)
- [ ] [04 — Branch sales](exercises/en/09_tuples/ex04_branch_sales.py)
- [ ] [05 — Support ticket summary](exercises/en/09_tuples/ex05_ticket_summary.py)
