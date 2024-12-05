from dataclasses import dataclass, field
from typing import Dict, List


@dataclass
class OrderingRule:
    page_x: int
    page_y: int

    @classmethod
    def parse(cls, rule: str) -> "OrderingRule":
        x, y = rule.strip().split("|")

        return cls(int(x), int(y))

    def is_satisfied(self, updated_pages: List[int]) -> bool:
        if self.page_x not in updated_pages or self.page_y not in updated_pages:
            return True

        idx_x = updated_pages.index(self.page_x)
        idx_y = updated_pages.index(self.page_y)

        return idx_x < idx_y


@dataclass
class OrderingRuleCollection:
    ordering_rules: Dict[int, List[OrderingRule]] = field(
        default_factory=dict, init=False
    )

    def add_rule(self, rule: str) -> None:
        new_rule = OrderingRule.parse(rule)

        if not new_rule.page_x in self.ordering_rules:
            self.ordering_rules[new_rule.page_x] = []

        self.ordering_rules[new_rule.page_x].append(new_rule)

    def check_ordering(self, updated_pages: List[int]) -> bool:
        for n in updated_pages:
            if not all(
                rule.is_satisfied(updated_pages)
                for rule in self.ordering_rules.get(n, [])
            ):
                return False

        return True

    def order_update(self, updated_pages: List[int]) -> List[int]:
        ordered_update = [n for n in updated_pages]

        rules: List[OrderingRule] = []
        for n in ordered_update:
            rules.extend(
                [
                    rule
                    for rule in self.ordering_rules.get(n, [])
                    if rule.page_y in ordered_update
                ]
            )

        rules_eval = [rule.is_satisfied(ordered_update) for rule in rules]

        try:
            idx = rules_eval.index(False)
        except ValueError:
            return ordered_update

        while idx != -1:
            idx_x = ordered_update.index(rules[idx].page_x)
            idx_y = ordered_update.index(rules[idx].page_y)
            ordered_update.pop(idx_x)
            ordered_update.insert(idx_y, rules[idx].page_x)

            rules_eval = [rule.is_satisfied(ordered_update) for rule in rules]

            try:
                idx = rules_eval.index(False)
            except ValueError:
                return ordered_update


if __name__ == "__main__":
    sum = 0
    rules = OrderingRuleCollection()
    # with open("./day05/example_input") as file:
    with open("./day05/input") as file:
        finished_rules = False
        for line in file:
            if not line.strip():
                finished_rules = True
                continue

            if not finished_rules:
                rules.add_rule(line)
            else:
                update = [int(n) for n in line.strip().split(",")]
                if not rules.check_ordering(update):
                    update = rules.order_update(update)
                    sum += update[round((len(update) - 1) / 2)]

    print(f"Sum of corrected updates middle page numbers: {sum}")
