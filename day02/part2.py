from typing import List


def check_deltas(report: List[int]) -> List[bool]:
    level_deltas = [report[i - 1] - report[i] for i in range(1, len(report))]

    delta_signs = [-1 if delta < 0 else 1 for delta in level_deltas]
    sign = -1 if sum(delta_signs) < 0 else 1

    return [1 <= (sign * delta) <= 3 for delta in level_deltas]


if __name__ == "__main__":
    safe_reports = 0
    # with open("./day02/example_input") as file:
    with open("./day02/input") as file:
        for line in file:
            report = [int(level) for level in line.strip().split(" ")]

            checked_deltas = check_deltas(report)

            if all(checked_deltas):
                safe_reports += 1
            else:
                idx = checked_deltas.index(False)

                alternative_reports = [
                    report[:idx] + report[idx + 1 :],
                    report[: idx + 1] + report[idx + 2 :],
                ]

                for report in alternative_reports:
                    if all(check_deltas(report)):
                        safe_reports += 1
                        break
    print(f"Total safe reports: {safe_reports}")
