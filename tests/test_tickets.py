# Tests for tickets.py. Run them with: pytest (in the exercise folder, with the virtual environment on).
# Each test runs tickets.py the way `python tickets.py` does, types the answers in its name (the day, the group
# size, then each person's age), and reads the numbered lines it prints, such as "1) Ticket for age 35: $36".
# A failing test says what it typed, the line it expected and the line tickets.py printed, or the error that
# stopped tickets.py.
# You don't need to change this file.
import os
import re
import subprocess
import sys
from pathlib import Path

import pytest

SCRIPT = Path(__file__).resolve().parent.parent / "tickets.py"


def typing(typed):
    """How a test's message starts: "Typing 'Maya', '3', '2', receipt.py", or just "menu.py" for a script that
    asks nothing, so the tests type nothing."""
    if not typed:
        return SCRIPT.name
    return "Typing " + ", ".join(repr(answer) for answer in typed) + ", " + SCRIPT.name


def run_script(*typed):
    """Runs the script with this Python, types each answer in typed followed by Enter, and returns what happened.
    A run still going after 10 seconds is stopped: a while loop that never ends is the usual reason."""
    __tracebackhide__ = True
    try:
        return subprocess.run(
            [sys.executable, str(SCRIPT)],
            input="".join(answer + "\n" for answer in typed),
            capture_output=True,
            text=True,
            encoding="utf-8",
            timeout=10,
            env={**os.environ, "PYTHONUTF8": "1"},  # the same text on every computer
        )
    except subprocess.TimeoutExpired:
        pass  # failed below, outside this except, so pytest shows only the message
    pytest.fail(
        f"{typing(typed)} was still running after 10 seconds, so the test stopped it. Look for a while loop that "
        "never ends: does the loop change, or ask again for, the value its condition checks?",
        pytrace=False,
    )


def printed_lines(result):
    """Each line the script printed that has a line number and ")", by that number:
    "1) name: Maya" -> {"1": "1) name: Maya"}.
    When the tests type the answers, nothing ends the question's line, so a numbered line can come right after a
    question, as in "How many sodas? 1) name: Maya". The number is found there too."""
    lines = {}
    for line in result.stdout.splitlines():
        match = re.search(r"(?:^|\s)(\w+)\)", line)
        if match:
            lines[match.group(1)] = line[match.start(1):].strip()
    return lines


def expect(condition, message):
    """Fails with just the message when the condition isn't true."""
    __tracebackhide__ = True  # pytest shows the message, not this helper's code
    if not condition:
        pytest.fail(message, pytrace=False)


def program_runs(result, typed=()):
    """Fails, with the end of Python's traceback, when the script stopped with an error."""
    __tracebackhide__ = True
    traceback_end = "\n".join([line for line in result.stderr.splitlines() if line.strip()][-4:])
    same_answers = ", type the same answers," if typed else ""
    expect(
        result.returncode == 0,
        f"{typing(typed)} stopped with an error. Run python {SCRIPT.name} in the terminal{same_answers} and read "
        "the traceback from its last line up:\n" + traceback_end,
    )


def check(typed, number, expected):
    """Fails unless the script, given these answers, ran to the end and printed exactly the line expected."""
    __tracebackhide__ = True
    result = run_script(*typed)
    program_runs(result, typed)
    lines = printed_lines(result)
    expect(number in lines, f"{typing(typed)} printed no line {number}. It should print: {expected}")
    got = lines[number]
    expect(got == expected, f"{typing(typed)} should print the line: {expected}\nbut it printed: {got}")


SATURDAY_GROUP = ["Saturday", "3", "35", "8", "2"]
TUESDAY_GROUP = ["Tuesday", "3", "12", "13", "70"]
SUNDAY_GROUP = ["sunday", "2", "3", "65"]
RE_ASKED_GROUP = ["Friday", "0", "9", "2", "10", "30"]


def test_1_saturday_age_35_ticket_is_36():
    check(SATURDAY_GROUP, "1", "1) Ticket for age 35: $36")


def test_2_saturday_age_8_ticket_is_24():
    check(SATURDAY_GROUP, "2", "2) Ticket for age 8: $24")


def test_3_saturday_age_2_ticket_is_free_0():
    check(SATURDAY_GROUP, "3", "3) Ticket for age 2: $0")


def test_4_saturday_group_of_3_aged_35_8_and_2_total_is_60():
    check(SATURDAY_GROUP, "4", "4) Group total: $60")


def test_5_tuesday_age_12_ticket_is_18():
    check(TUESDAY_GROUP, "1", "1) Ticket for age 12: $18")


def test_6_tuesday_age_13_ticket_is_30():
    check(TUESDAY_GROUP, "2", "2) Ticket for age 13: $30")


def test_7_tuesday_age_70_ticket_is_20():
    check(TUESDAY_GROUP, "3", "3) Ticket for age 70: $20")


def test_8_tuesday_group_of_3_aged_12_13_and_70_total_is_68():
    check(TUESDAY_GROUP, "4", "4) Group total: $68")


def test_9_sunday_age_3_ticket_is_24():
    check(SUNDAY_GROUP, "1", "1) Ticket for age 3: $24")


def test_10_sunday_age_65_ticket_is_26():
    check(SUNDAY_GROUP, "2", "2) Ticket for age 65: $26")


def test_11_monday_group_of_1_aged_40_total_is_30():
    check(["Monday", "1", "40"], "2", "2) Group total: $30")


def test_12_group_size_0_then_9_prints_groups_are_1_to_8_people_twice():
    result = run_script(*RE_ASKED_GROUP)
    program_runs(result, RE_ASKED_GROUP)
    times = result.stdout.count("Groups are 1 to 8 people.")
    expect(
        times == 2,
        f"{typing(RE_ASKED_GROUP)} should print 'Groups are 1 to 8 people.' twice, once for 0 and once for 9, "
        f"but it printed it {times} time(s).",
    )


def test_13_after_0_and_9_a_friday_group_of_2_aged_10_and_30_total_is_48():
    check(RE_ASKED_GROUP, "3", "3) Group total: $48")


def test_14_wednesday_group_of_8_aged_30_is_allowed_and_totals_240():
    check(["Wednesday", "8"] + ["30"] * 8, "9", "9) Group total: $240")
