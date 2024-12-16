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


def brute_force_pt1(puzzle: list[str]) -> int:  # noqa: C901
    count = 0
    height = len(puzzle)
    width = len(puzzle[0])
    for y in range(height):
        for x in range(width):
            # find starting point at X
            if puzzle[y][x] == "X":
                # up
                if y >= 3 and puzzle[y - 1][x] + puzzle[y - 2][x] + puzzle[y - 3][x] == "MAS":
                    count += 1
                # up and left
                if y >= 3 and x >= 3 and puzzle[y - 1][x - 1] + puzzle[y - 2][x - 2] + puzzle[y - 3][x - 3] == "MAS":
                    count += 1
                # up and right
                if (
                    y >= 3
                    and x <= width - 4
                    and puzzle[y - 1][x + 1] + puzzle[y - 2][x + 2] + puzzle[y - 3][x + 3] == "MAS"
                ):
                    count += 1
                # left
                if x >= 3 and puzzle[y][x - 1] + puzzle[y][x - 2] + puzzle[y][x - 3] == "MAS":
                    count += 1
                # right
                if x <= width - 4 and puzzle[y][x + 1] + puzzle[y][x + 2] + puzzle[y][x + 3] == "MAS":
                    count += 1
                # down
                if y <= height - 4 and puzzle[y + 1][x] + puzzle[y + 2][x] + puzzle[y + 3][x] == "MAS":
                    count += 1
                # down and left
                if (
                    y <= height - 4
                    and x >= 3
                    and puzzle[y + 1][x - 1] + puzzle[y + 2][x - 2] + puzzle[y + 3][x - 3] == "MAS"
                ):
                    count += 1
                # down and right
                if (
                    y <= height - 4
                    and x <= width - 4
                    and puzzle[y + 1][x + 1] + puzzle[y + 2][x + 2] + puzzle[y + 3][x + 3] == "MAS"
                ):
                    count += 1
    return count


def brute_force_pt2(puzzle: list[str]) -> int:
    count = 0
    height = len(puzzle)
    width = len(puzzle[0])
    for y in range(height):
        for x in range(width):
            # find starting point at A
            if puzzle[y][x] == "A":
                # MM
                # SS
                if (
                    width - 2 >= x >= 1
                    and height - 2 >= y >= 1
                    and puzzle[y - 1][x - 1] == "M"
                    and puzzle[y - 1][x + 1] == "M"
                    and puzzle[y + 1][x - 1] == "S"
                    and puzzle[y + 1][x + 1] == "S"
                ):
                    count += 1
                # SS
                # MM
                if (
                    width - 2 >= x >= 1
                    and height - 2 >= y >= 1
                    and puzzle[y - 1][x - 1] == "S"
                    and puzzle[y - 1][x + 1] == "S"
                    and puzzle[y + 1][x - 1] == "M"
                    and puzzle[y + 1][x + 1] == "M"
                ):
                    count += 1
                # MS
                # MS
                if (
                    width - 2 >= x >= 1
                    and height - 2 >= y >= 1
                    and puzzle[y - 1][x - 1] == "M"
                    and puzzle[y - 1][x + 1] == "S"
                    and puzzle[y + 1][x - 1] == "M"
                    and puzzle[y + 1][x + 1] == "S"
                ):
                    count += 1
                # SM
                # SM
                if (
                    width - 2 >= x >= 1
                    and height - 2 >= y >= 1
                    and puzzle[y - 1][x - 1] == "S"
                    and puzzle[y - 1][x + 1] == "M"
                    and puzzle[y + 1][x - 1] == "S"
                    and puzzle[y + 1][x + 1] == "M"
                ):
                    count += 1
    return count


def test_04a_sample() -> None:
    count = brute_force_pt1(SAMPLE_INPUT.splitlines())
    assert count == 18


def test_04a(day04_lines: str) -> None:
    count = brute_force_pt1(day04_lines)
    assert count == 2454


def test_04b_sample() -> None:
    count = brute_force_pt2(SAMPLE_INPUT.splitlines())
    assert count == 9


def test_04b(day04_lines: str) -> None:
    count = brute_force_pt2(day04_lines)
    assert count == 1858
