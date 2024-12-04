MUL_LP = "mul("
COMMA = ","
RP = ")"


def operate_muls_in_line(line: str) -> int:
    i = line.find(MUL_LP)
    if i < 0:
        return 0
    line = line[i + len(MUL_LP) :]
    i = line.find(COMMA)
    if i < 0:
        return 0
    elif i == 0:
        return operate_muls_in_line(line)
    first_number = line[:i]
    if not all(c.isdigit() for c in first_number):
        return operate_muls_in_line(line)
    first_number = int(first_number)
    line = line[i + 1 :]
    i = line.find(RP)
    if i < 0:
        return 0
    elif i == 0:
        return operate_muls_in_line(line)
    second_number = line[:i]
    if not all(c.isdigit() for c in second_number):
        return operate_muls_in_line(line)
    second_number = int(second_number)
    line = line[i + 1 :]
    if line:
        return first_number * second_number + operate_muls_in_line(line)
    else:
        return first_number * second_number


if __name__ == "__main__":
    sum = 0
    # with open("./day03/example_input") as file:
    with open("./day03/input") as file:
        for line in file:
            sum += operate_muls_in_line(line)
    print(f"Sum of multiplications: {sum}")
