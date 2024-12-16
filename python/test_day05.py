from collections import defaultdict

SAMPLE_INPUT = """47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47"""


def parse_input(in_string: str) -> list[tuple[str, str], list[tuple[str, ...]]]:
    rules: list[tuple[str, str]] = []
    updates: list[tuple[str]] = []
    for line in in_string.splitlines():
        if "|" in line:
            left, right = line.strip().split("|")
            rules.append((left, right))

        if "," in line:
            updates.append(tuple(line.strip().split(",")))

    return rules, updates


def get_valid_rules(rules: list[tuple[str, str]], update: tuple[str, ...]) -> list[tuple[str, str]]:
    return [rule for rule in rules if set(rule).issubset(set(update))]


def order_pages(rules: list[tuple[str, str]]) -> list[str]:
    rule_dict: defaultdict[str] = defaultdict(list)
    for rule in rules:
        rule_dict[rule[0]].append(rule[1])
    for page in rule_dict.values():
        if len(page) == 1:
            last_page = page[0]

    return (*sorted(rule_dict, key=lambda key: len(rule_dict[key]), reverse=True), last_page)


def is_update_valid(pages: list[str], rules: defaultdict[list[str]]) -> bool:
    while len(pages) > 1:
        current_page = pages.pop(0)
        for page in pages:
            if page not in rules[current_page]:
                return False

    return True


def test_05a_sample() -> None:
    rules, updates = parse_input(SAMPLE_INPUT)
    result = 0

    for update in updates:
        valid_rules = get_valid_rules(rules, update)
        ordered_pages = order_pages(valid_rules)

        if update == ordered_pages:
            result += int(update[len(update) // 2])

    assert result == 143


def test_05a(day05_text: str) -> None:
    rules, updates = parse_input(day05_text)
    result = 0

    for update in updates:
        valid_rules = get_valid_rules(rules, update)
        ordered_pages = order_pages(valid_rules)

        if update == ordered_pages:
            result += int(update[len(update) // 2])

    assert result == 4957


def test_05b_sample() -> None:
    rules, updates = parse_input(SAMPLE_INPUT)

    result = 0

    for update in updates:
        valid_rules = get_valid_rules(rules, update)
        ordered_pages = order_pages(valid_rules)

        if update != ordered_pages:
            result += int(ordered_pages[len(update) // 2])

    assert result == 123


def test_05b(day05_text: str) -> None:
    rules, updates = parse_input(day05_text)

    result = 0

    for update in updates:
        valid_rules = get_valid_rules(rules, update)
        ordered_pages = order_pages(valid_rules)

        if update != ordered_pages:
            result += int(ordered_pages[len(update) // 2])

    assert result == 6938
