# Exercise: Water Park Tickets

Exercise code for the lesson **Exercise: Water Park Tickets** in the Python in Depth course on [ask-codey.com](https://www.ask-codey.com).

The ticket booth at Splash Valley Water Park prices a whole group at once. `tickets.py` already asks for the day of the visit and how many people are in the group. You'll check the group's size, ask each person's age, print each ticket's price, and print the group's total. The tests run your script, type the answers in for you, and check each numbered line it prints.

## What's here

- `tickets.py`: the prices in a comment, the first two questions, and the four steps to write. For you to finish.
- `tests/test_tickets.py`: tests that run `tickets.py`, type the answers in, and check the numbered lines it prints. You don't need to change this file.
- `requirements.txt`: the one package the tests need, pytest, at an exact version. Ready to use.
- `pytest.ini`: tells pytest where the tests are. Ready to use.
- `.gitignore`: tells Git to leave out the virtual environment and the files Python and pytest make as they run. Ready to use.

## Before you start

The tests need pytest, and pytest goes in a virtual environment: a private set of packages for this folder only. In VS Code's terminal, in this folder, run these three commands.

On Windows (PowerShell):

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

On a Mac (zsh):

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

- The first command makes the virtual environment, in a folder named `.venv`.
- The second turns it on for this terminal: the prompt starts with `(.venv)` from then on.
- The third installs the packages `requirements.txt` lists into it: here, only pytest.

*Virtual Environments and pip*, in Module 3, explains all three. The `.venv` folder is in `.gitignore`, so Git leaves it out: these commands make it again on any computer.

If PowerShell answers that running scripts is disabled on this system, run this once, then run the second command again:

```powershell
Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned
```

Each new terminal starts with the virtual environment off. If the prompt doesn't start with `(.venv)`, run the second command again. (VS Code often turns it on for you.)

## What to print

One numbered line for each ticket, then one for the group's total. Each line is a number, a closing parenthesis, a name and a value. Typing `Saturday`, `3`, then the ages `35`, `8` and `2`, the lines are:

```text
1) Ticket for age 35: $36
2) Ticket for age 8: $24
3) Ticket for age 2: $0
4) Group total: $60
```

## The rules

- **The prices:** under 3 is free ($0), 3 to 12 is $18, 13 to 64 is $30, and 65 and over is $20.
- **The weekend:** on a Saturday or a Sunday, every ticket that isn't free costs $6 more. A free ticket stays $0. `tickets.py` already turns the day into lowercase, so `Saturday` arrives as `saturday`.
- **The group's size:** a group is 1 to 8 people. While the size typed is less than 1 or more than 8, print `Groups are 1 to 8 people.` and ask again, with the same question. A group of 8 is fine.
- **The ages:** ask each person's age with `age = int(input(f"How old is person {person}? "))`, numbering the people from 1.
- **Each ticket's line:** the person's number, `) Ticket for age `, the age, `: $` and the price, such as `2) Ticket for age 8: $24`.
- **The total's line:** after the last ticket, one more than the group's size, `) Group total: $` and the total, such as `4) Group total: $60`.
- Keep the first two questions as they are, in their order: the tests type the day, then the group's size (again, until it's 1 to 8), then each age. Don't change the tests.

The tests type these answers, and check these lines:

| Typed | Lines checked |
|---|---|
| `Saturday`, `3`, `35`, `8`, `2` | `1) Ticket for age 35: $36`, `2) Ticket for age 8: $24`, `3) Ticket for age 2: $0`, `4) Group total: $60` |
| `Tuesday`, `3`, `12`, `13`, `70` | `1) Ticket for age 12: $18`, `2) Ticket for age 13: $30`, `3) Ticket for age 70: $20`, `4) Group total: $68` |
| `sunday`, `2`, `3`, `65` | `1) Ticket for age 3: $24`, `2) Ticket for age 65: $26` |
| `Monday`, `1`, `40` | `2) Group total: $30` |
| `Friday`, `0`, `9`, `2`, `10`, `30` | `Groups are 1 to 8 people.` printed twice, and `3) Group total: $48` |
| `Wednesday`, `8`, then `30` eight times | `9) Group total: $240` |

## Check your work

```bash
pytest
```

At first every test fails: that is expected, because `tickets.py` doesn't print any tickets yet. Each line you print correctly turns its tests green. A failing test's message says what it typed, the line it expected and what came back, for example:

```text
Typing 'Saturday', '3', '35', '8', '2', tickets.py should print the line: 3) Ticket for age 2: $0
but it printed: 3) Ticket for age 2: $6
```

A test that says *tickets.py was still running after 10 seconds* has found a `while` loop that never ends.

To try it yourself, run it and type the answers:

```bash
python tickets.py
```

## Tips

- Work one group through by hand first: on a Saturday, a 35-year-old's $30 ticket becomes $36, an 8-year-old's $18 becomes $24, and a 2-year-old's stays free, so the total is $60.
- `input()` gives back text, and `int()` turns it into a whole number. The questions in `tickets.py` already do both.
- Check the ages from the youngest up with `if`, `elif` and `else`, so each age reaches the right price.
- `and` joins two conditions that must both be true: it's the weekend, and the ticket isn't free.
- `range(1, group_size + 1)` counts from 1 up to the group's size, because `range` leaves its stop out.
- Start the total at 0 before the loop, and add each price to it inside the loop with `+=`.

## Hand it in

When it works, push your solution to a public repo of your own on GitHub, then paste that repo's address into **Submit your exercise** on the lesson page at [ask-codey.com](https://www.ask-codey.com). That's what completes the lesson. The lesson page shows the Git commands, step by step.
