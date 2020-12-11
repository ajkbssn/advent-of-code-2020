# /src/advent_of_code/dec11.py

import copy
import matplotlib.pyplot as plt

# constants
mapdict = {".": 0, "L": 1, "#": 2, "+": -3}
# empty seat = "L"
# occupied seat = "#"
# floor = "."
leave_limit = 5


def loadwaitingarea(filename):
    with open(filename) as f:
        lines = f.readlines()
    grid = []
    wall = [mapdict["+"]]
    for pixel in lines[0].strip():
        wall.append(mapdict["+"])
    wall.append(mapdict["+"])
    grid.append(wall)
    for line in lines:
        line = line.strip()
        row = [mapdict["+"]]
        for pixel in line:
            row.append(mapdict[pixel])
        row.append(mapdict["+"])
        grid.append(row)
    grid.append(wall)
    return grid


def neigbors(grid):
    neighbor_grid = copy.deepcopy(grid)
    for y in range(1, len(grid) - 1):
        for x in range(1, len(grid[0]) - 1):
            if grid[y][x] != mapdict["."]:
                n0 = -[grid[y][x]].count(mapdict["#"])
                n0 += grid[y - 1][x - 1 : x + 2].count(mapdict["#"])
                n0 += grid[y][x - 1 : x + 2].count(mapdict["#"])
                n0 += grid[y + 1][x - 1 : x + 2].count(mapdict["#"])
                neighbor_grid[y][x] = n0
    return neighbor_grid


def neighbors_longer(grid):
    neighbor_grid = copy.deepcopy(grid)
    for y in range(1, len(grid) - 1):
        for x in range(1, len(grid[0]) - 1):
            if grid[y][x] != mapdict["."]:
                # nw
                further = True
                s = 0
                while further:
                    s += 1
                    cell = grid[y - s][x - s]
                    if cell != mapdict["."]:
                        further = False
                        if cell == mapdict["#"]:
                            n0 = 1
                        else:
                            n0 = 0
                # n
                further = True
                s = 0
                while further:
                    s += 1
                    cell = grid[y - s][x]
                    if cell != mapdict["."]:
                        further = False
                        if cell == mapdict["#"]:
                            n0 += 1
                # ne
                further = True
                s = 0
                while further:
                    s += 1
                    cell = grid[y - s][x + s]
                    if cell != mapdict["."]:
                        further = False
                        if cell == mapdict["#"]:
                            n0 += 1
                # e
                further = True
                s = 0
                while further:
                    s += 1
                    cell = grid[y][x + s]
                    if cell != mapdict["."]:
                        further = False
                        if cell == mapdict["#"]:
                            n0 += 1
                # se
                further = True
                s = 0
                while further:
                    s += 1
                    cell = grid[y + s][x + s]
                    if cell != mapdict["."]:
                        further = False
                        if cell == mapdict["#"]:
                            n0 += 1
                # s
                further = True
                s = 0
                while further:
                    s += 1
                    cell = grid[y + s][x]
                    if cell != mapdict["."]:
                        further = False
                        if cell == mapdict["#"]:
                            n0 += 1
                # sw
                further = True
                s = 0
                while further:
                    s += 1
                    cell = grid[y + s][x - s]
                    if cell != mapdict["."]:
                        further = False
                        if cell == mapdict["#"]:
                            n0 += 1
                # w
                further = True
                s = 0
                while further:
                    s += 1
                    cell = grid[y][x - s]
                    if cell != mapdict["."]:
                        further = False
                        if cell == mapdict["#"]:
                            n0 += 1
                neighbor_grid[y][x] = n0
    return neighbor_grid


def update_grid(old_grid):
    new_grid = copy.deepcopy(old_grid)
    occ_grid = neighbors_longer(old_grid)
    changes = 0

    for y in range(1, len(old_grid) - 1):
        for x in range(1, len(old_grid[0]) - 1):
            if old_grid[y][x] == mapdict["L"] and occ_grid[y][x] == 0:
                new_grid[y][x] = mapdict["#"]
                changes += 1
            if old_grid[y][x] == mapdict["#"] and occ_grid[y][x] >= leave_limit:
                new_grid[y][x] = mapdict["L"]
                changes += 1
    return new_grid, changes


def equilibrium(grid, showchart=False):
    if showchart:
        chart(grid)
    iterations = 0
    changes = 100000
    while iterations < 10000 and changes > 0:
        grid, changes = update_grid(grid)
        if showchart:
            chart(grid)
        iterations += 1
    if showchart:
        chart(grid, showchart)
    return iterations, grid


def count_cells(grid):
    count_occ = 0
    count_free = 0
    count_wall = 0
    count_floor = 0
    for row in grid:
        count_occ += row.count(mapdict["#"])
        count_free += row.count(mapdict["L"])
        count_floor += row.count(mapdict["."])
        count_wall += row.count(mapdict["+"])
    return count_occ, count_free, count_floor, count_wall


def actual_neighbors(grid):
    neighbor_grid = copy.deepcopy(grid)
    for y in range(1, len(grid) - 1):
        for x in range(1, len(grid[0]) - 1):
            if grid[y][x] == mapdict["#"]:
                occ = grid[y - 1][x - 1 : x + 2].count(mapdict["#"])
                occ += [grid[y][x - 1]].count(mapdict["#"])
                occ += [grid[y][x + 1]].count(mapdict["#"])
                occ += grid[y - 1][x - 1 : x + 2].count(mapdict["#"])
                neighbor_grid[y][x] = occ
            else:
                neighbor_grid[y][x] = 0
    return neighbor_grid


def chart(grid, keep=False):
    im = plt.imshow(grid)
    if keep:
        plt.show()


def test1():
    grid = loadwaitingarea("dec11_input.txt")  # ./src/advent_of_code_2020/
    # grid = loadwaitingarea("dec11_test.txt")  # ./src/advent_of_code_2020/
    itr, grid = equilibrium(grid, True)
    X = count_cells(grid)
    print(X)


test1()
