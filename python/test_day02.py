from itertools import pairwise

SAMPLE_DATA = """7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9"""


def safe_increase(input: list[int]) -> bool:
    # subsequent elements must increase by 1 to 3
    steps = [b - a for a, b in pairwise(input)]
    return all(1 <= n <= 3 for n in steps)


def safe_decrease(input: list[int]) -> bool:
    # subsequent elements must decrease by 1 to 3
    steps = [a - b for a, b in pairwise(input)]
    return all(1 <= n <= 3 for n in steps)


def safe_row(row: list[int]) -> bool:
    return safe_increase(row) or safe_decrease(row)


def count_safe(rows: list[list[int]]) -> int:
    return sum(safe_row(row) for row in rows)


def try_safe(row: list[int]) -> bool:
    for n in range(len(row)):
        temp_row = row.copy()
        temp_row.pop(n)
        if safe_row(temp_row):
            return True
    return False



def test_02a_sample():
    rows = []
    for line in SAMPLE_DATA.splitlines():
        row = [int(n) for n in line.split()]
        rows.append(row)

    safe = count_safe(rows)

    assert safe == 2


def test_02a(day02_number_grid):
    safe = count_safe(day02_number_grid)

    assert safe == 559


def test_02b_sample():
    rows = []
    for line in SAMPLE_DATA.splitlines():
        row = [int(n) for n in line.split()]
        rows.append(row)

    unsafe_rows = [row for row in rows if not safe_row(row)]

    safe = len(rows) - len(unsafe_rows)
    for row in unsafe_rows:
        if try_safe(row):
            safe += 1
    
    assert safe == 4


def test_02b(day02_number_grid):
    unsafe_rows = [row for row in day02_number_grid if not safe_row(row)]
    safe = len(day02_number_grid) - len(unsafe_rows)
    for row in unsafe_rows:
        if try_safe(row):
            safe += 1
    
    assert safe == 601

