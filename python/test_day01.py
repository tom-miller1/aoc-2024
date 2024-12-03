from collections import Counter


SAMPLE_DATA = """3   4
4   3
2   5
1   3
3   9
3   3"""


def calculate_distance(input: list[str]) -> int:
    col1 = []
    col2 = []
    for line in input:
        val1, val2 = line.split()
        col1.append(int(val1))
        col2.append(int(val2))
    return sum(abs(element[0] - element[1]) for element in zip(sorted(col1), sorted(col2)))


def calculate_similarity(input: list[str]) -> int:
    col1 = []
    col2 = Counter()
    for line in input:
        val1, val2 = line.split()
        col1.append(int(val1))
        col2[int(val2)] += 1
    return sum(element * col2[element] for element in col1)


def test_01a_sample():
    lines = SAMPLE_DATA.splitlines()
    assert calculate_distance(lines) == 11


def test_01b_sample():
    lines = SAMPLE_DATA.splitlines()
    assert calculate_similarity(lines) == 31


def test_01a(day01_lines):
    assert calculate_distance(day01_lines) == 1388114


def test_01b(day01_lines):
    assert calculate_similarity(day01_lines) == 23529853
