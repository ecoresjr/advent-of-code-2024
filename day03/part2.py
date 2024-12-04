from typing import Tuple

MUL_LP = "mul("
COMMA = ","
RP = ")"
DO = "do()"
DONT = "don't()"


def operate_conditionals_until_mul_is_found(
    line: str, do: bool = True
) -> Tuple[str, bool, int]:
    j = line.find(MUL_LP)

    while j >= 0:
        k = line.find(DO)
        k = k if k >= 0 else j

        l = line.find(DONT)
        l = l if l >= 0 else j

        i = min(j, k, l)

        if i == j:
            break
        elif i == k:
            do = True
            line = line[i + len(DO) :]
        elif i == l:
            do = False
            line = line[i + len(DONT) :]

        j = line.find(MUL_LP)

    return line, do, j


def operate_muls_in_line(line: str, do: bool = True) -> Tuple[int, bool]:
    line, do, i = operate_conditionals_until_mul_is_found(line, do)
    if i < 0:
        return 0, do
    line = line[i + len(MUL_LP) :]
    i = line.find(COMMA)
    if i < 0:
        return 0, do
    elif i == 0:
        return operate_muls_in_line(line, do)
    first_number = line[:i]
    if not all(c.isdigit() for c in first_number):
        return operate_muls_in_line(line, do)
    first_number = int(first_number)
    line = line[i + 1 :]
    i = line.find(RP)
    if i < 0:
        return 0, do
    elif i == 0:
        return operate_muls_in_line(line, do)
    second_number = line[:i]
    if not all(c.isdigit() for c in second_number):
        return operate_muls_in_line(line, do)
    second_number = int(second_number)
    line = line[i + 1 :]
    if line:
        mul, last_do = operate_muls_in_line(line, do)
        return ((first_number * second_number if do else 0) + mul), last_do
    else:
        return (first_number * second_number if do else 0), do


if __name__ == "__main__":
    sum = 0
    do = True
    # with open("./day03/example_input_part2") as file:
    with open("./day03/input") as file:
        for line in file:
            partial_sum, do = operate_muls_in_line(line, do)
            sum += partial_sum
    print(f"Sum of multiplications: {sum}")
