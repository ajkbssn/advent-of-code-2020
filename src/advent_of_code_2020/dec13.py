# src/..


def load_shuttles(filename):
    with open(filename) as f:
        lines = f.readlines()
    return [line.strip() for line in lines]


def get_shuttles(line):

    shuttles = [[int(elem), i] for i, elem in enumerate(line.split(",")) if elem != "x"]
    return shuttles


def chinese_remainder_buses(shuttles):
    bigM = 1
    for s1 in shuttles:
        bigM *= s1[0]
    M = [int(bigM / s2[0]) for s2 in shuttles]
    a = [(s3[0] - s3[1]) % s3[0] for s3 in shuttles]
    y = []
    for i in range(len(shuttles)):
        tmp = M[i] % shuttles[i][0]
        x = 1
        while x * tmp % shuttles[i][0] != 1:
            x += 1
        y.append(int(x))
    X = 0
    for i in range(len(shuttles)):
        X += a[i] * y[i] * M[i]
        X = X % bigM
    return X, a, y, M, bigM


def next_alignment(bus0, delay0, bus1, delay1):
    base = delay0
    while True:
        base += bus0
        if base % bus1 == delay1:
            return base


def y2020_13_part2(data):
    busses = data[1].split(",")
    base = 0
    baseid = int(busses[0])
    for idx, busid in enumerate(busses[1:], start=1):
        if busid == "x":
            continue
        busid = int(busid)
        busidx = (busid - idx) % busid

        print(f"call next_alignment: {baseid}, {base}, {busid}, {busidx}")
        alignment = next_alignment(baseid, base, busid, busidx)
        print(f"all busses so far align to {alignment}")
        baseid *= busid
        base = alignment - baseid
    return alignment


sh = load_shuttles("dec13_input.txt")
# sh = load_shuttles("dec13_test1.txt")
# print(f"Part 2: bus alignment occurs at {y2020_13_part2(sh)}")

# print(sh)
s1 = get_shuttles(sh[1])

# print(sh)
# s1 = [[3, 1], [5, 2], [7, 5]]
# print(s1)
# print()
X, a, y, M, bigM = chinese_remainder_buses(s1)
print(f"X är {X}")
# print(f"a är {a}")
print(y)
print(M)
# print(bigM)
# for sh in s1:
#    for sh2 in s1:
#        print(f"{sh[0]%sh2[0]:3}", end=" ")
#    print()
