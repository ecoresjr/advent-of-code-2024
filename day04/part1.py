from typing import List, Tuple

XMAS = "XMAS"


def find_word(
    grid: List[str], word: str, start: Tuple[int, int], direction: Tuple[int, int]
) -> bool:
    i, j = start
    di, dj = direction
    for n in range(1, len(word)):
        if grid[i + di * n][j + dj * n] != word[n]:
            return False
    return True


if __name__ == "__main__":
    count = 0

    grid = []
    # with open("./day04/example_input") as file:
    with open("./day04/input") as file:
        for line in file:
            grid.append(line.strip())

    rows = len(grid)
    columns = len(grid[0])
    w_len = len(XMAS)

    for i in range(rows):
        for j in range(columns):
            if grid[i][j] != XMAS[0]:
                continue

            up = i >= w_len - 1
            down = i <= rows - w_len
            left = j >= w_len - 1
            right = j <= columns - w_len

            if up and find_word(grid, XMAS, (i, j), (-1, 0)):
                count += 1
            if up and left and find_word(grid, XMAS, (i, j), (-1, -1)):
                count += 1
            if up and right and find_word(grid, XMAS, (i, j), (-1, 1)):
                count += 1
            if down and find_word(grid, XMAS, (i, j), (1, 0)):
                count += 1
            if down and left and find_word(grid, XMAS, (i, j), (1, -1)):
                count += 1
            if down and right and find_word(grid, XMAS, (i, j), (1, 1)):
                count += 1
            if left and find_word(grid, XMAS, (i, j), (0, -1)):
                count += 1
            if right and find_word(grid, XMAS, (i, j), (0, 1)):
                count += 1

    print(f"{XMAS} occurrences: {count}")
