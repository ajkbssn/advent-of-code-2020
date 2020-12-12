def path(grid, step):
    xs, ys = step
    p0 = []
    x, y = 0, 0
    width = len(grid[0])
    length = len(grid)
    while y < length:
        p0.append(grid[y][x % width])
        x += xs
        y += ys
    return p0


def loadterrain(filename):
    with open(filename) as f:
        lines = f.readlines()
    return [line.strip() for line in lines]


ter = loadterrain("dec03_input.txt")
p_list = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
prod = 1
for p in p_list:
    prod *= path(ter, p).count("#")
print(prod)
