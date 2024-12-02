if __name__ == "__main__":
    safe_reports = 0
    # with open("./day02/example_input") as file:
    with open("./day02/input") as file:
        for line in file:
            report = [int(level) for level in line.strip().split(" ")]
            level_deltas = [report[i - 1] - report[i] for i in range(1, len(report))]
            sign = 1
            if level_deltas[0] < 0:
                sign = -1
            if all([1 <= (sign * delta) <= 3 for delta in level_deltas]):
                safe_reports += 1
    print(f"Total safe reports: {safe_reports}")
