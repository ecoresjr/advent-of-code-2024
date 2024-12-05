from typing import List, Tuple

MAS = "MAS"


def find_word(
    grid: List[str],
    word: str,
    start: Tuple[int, int],
    direction: Tuple[int, int],
    res_grid: List[List[int]],
) -> bool:
    i, j = start
    di, dj = direction
    for n in range(1, len(word)):
        if grid[i + di * n][j + dj * n] != word[n]:
            return False

    res_grid[i + di][j + dj] += 1

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
    w_len = len(MAS)
    res_grid = [[0 for _ in range(columns)] for _ in range(rows)]

    for i in range(rows):
        for j in range(columns):
            if grid[i][j] != MAS[0]:
                continue

            up = i >= w_len - 1
            down = i <= rows - w_len
            left = j >= w_len - 1
            right = j <= columns - w_len

            if up and left:
                find_word(grid, MAS, (i, j), (-1, -1), res_grid)
            if up and right:
                find_word(grid, MAS, (i, j), (-1, 1), res_grid)
            if down and left:
                find_word(grid, MAS, (i, j), (1, -1), res_grid)
            if down and right:
                find_word(grid, MAS, (i, j), (1, 1), res_grid)

    for i in range(rows):
        for j in range(columns):
            if res_grid[i][j] == 2:
                count += 1

    print(f"X-MAS occurrences: {count}")
