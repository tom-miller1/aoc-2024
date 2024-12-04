import re

SAMPLE_INPUT = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"
SAMPLE_INPUT2 = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"


def parse_input(token_stream: str) -> int:
    mul_sum = 0
    if matches := re.finditer(r"mul\((\d{1,3}),(\d{1,3})\)", token_stream):
        for match in matches:
            mul_sum += int(match.group(1)) * int(match.group(2))
    return mul_sum


def test_03a_sample() -> None:
    assert parse_input(SAMPLE_INPUT) == 161


def test_03a(day03_text) -> None:  # noqa: ANN001
    assert parse_input(day03_text) == 161289189


def test_03b_sample() -> None:
    trimmed_input = re.sub(r"don't\(\).*do\(\)", "", SAMPLE_INPUT2)
    assert parse_input(trimmed_input) == 48


def test_03b(day03_text) -> None:  # noqa: ANN001
    trimmed_input = re.sub(r"don't\(\).*?do\(\)", "", day03_text, flags=re.DOTALL)
    assert parse_input(trimmed_input) == 83595109
