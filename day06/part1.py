GUARD = "^"
OBSTACLE = "#"
START_DIRECTION = (-1, 0)  # ^
TURN_90 = {
    (-1, 0): (0, 1),  # ^ : >
    (0, 1): (1, 0),  # > : v
    (1, 0): (0, -1),  # v : <
    (0, -1): (-1, 0),  # < : ^
}

if __name__ == "__main__":
    grid = []

    i = -1
    j = -1

    # with open("./day06/example_input") as file:
    with open("./day06/input") as file:
        for line in file:
            line = line.strip()
            grid.append(line)

            if j == -1:
                i += 1
                j = line.find(GUARD)

    di, dj = START_DIRECTION
    visited = set()
    while True:
        visited.add((i, j))

        while (
            i + di != len(grid)
            and i + di >= 0
            and j + dj != len(grid[0])
            and j + dj >= 0
            and grid[i + di][j + dj] == "#"
        ):
            di, dj = TURN_90[(di, dj)]

        if i + di == len(grid) or i + di < 0 or j + dj == len(grid[0]) or j + dj < 0:
            break

        i += di
        j += dj

    print(f"Distinct positions visited by the guard: {len(visited)}")
