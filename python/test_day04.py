import re

SAMPLE_INPUT = """MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX"""


def input_to_array(grid: str) -> list[list[str]]:
    return [list(line) for line in grid.splitlines()]


def rotate90(puzzle: list[list[str]]) -> list[list[str]]:
    result = []
    for n in range(len(puzzle[0])):
        result.append([])
        for m in range(len(puzzle)):
            result[n].append(puzzle[m][n])
    return result


def rotate45(puzzle: list[list[str]]) -> list[list[str]]:
    m = len(puzzle)
    n = len(puzzle[0])
    result = [[] for _ in range(m + n - 1)]
    # first half
    for y in range(m):
        diagonal_elements = min(m - 1, y, n - 1)
        diagonal_cnt = 0
        while y <= m - 1 and diagonal_elements >= 0:
            result[y].append(puzzle[y - diagonal_cnt][diagonal_cnt])
            diagonal_cnt += 1
            diagonal_elements -= 1
    # second half
    for x in range(1, n):
        diagonal_elements = min(m - 1, n - x - 1)
        diagonal_cnt = 0
        while x <= n - 1 and diagonal_elements >= 0:
            result[m + x - 1].append(puzzle[m - 1 - diagonal_cnt][x + diagonal_cnt])
            diagonal_cnt += 1
            diagonal_elements -= 1
    return result


def count_matches(array: list[list[str]]) -> int:
    count = 0
    for line in array:
        text = "".join(line)
        if matches := re.findall(r"(?=(XMAS|SAMX))", text):
            count += len(matches)
    return count


def test_01a_sample() -> None:
    puzzle = input_to_array(SAMPLE_INPUT)
    count = count_matches(puzzle)
    count += count_matches(rotate90(puzzle))
    count += count_matches(rotate45(puzzle))
    count += count_matches(rotate45(rotate90(puzzle)))
    assert count == 18


def test_01a(day04_text) -> None:
    from pprint import pprint

    puzzle = input_to_array(day04_text)
    count = count_matches(puzzle)
    print(count)
    count += count_matches(rotate90(puzzle))
    print(count)
    count += count_matches(rotate45(puzzle))
    pprint(rotate45(puzzle), width=800)
    print(count)
    count += count_matches(rotate45(rotate90(puzzle)))
    assert count == 2508
