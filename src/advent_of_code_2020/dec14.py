# src/


def loadprogram(filename):
    with open(filename, "r") as f:
        return [line.split("=") for line in f.readlines()]


def execute1(prog):
    mem = {}
    for line in prog:
        line[0] = line[0].strip()
        line[1] = line[1].strip()
        if line[0] == "mask":
            ormask = int(line[1].replace("X", "0").strip(), 2)
            andmask = int(line[1].replace("X", "1").strip(), 2)
        else:
            address = line[0].removeprefix("mem[")
            address = address.removesuffix("]")
            address = int(address)
            value = int(line[1])
            value = value | ormask
            value = value & andmask
            mem[address] = value
    return mem


def findX(mask):
    return [len(mask) - i - 1 for i, ch in enumerate(mask) if ch == "X"]


def execute2(prog):
    mem = {}
    for line in prog:
        line[0] = line[0].strip()
        line[1] = line[1].strip()
        if line[0] == "mask":
            volatile = findX(line[1])
            ormask = int(line[1].replace("X", "0").strip(), 2)
        else:
            value = int(line[1])
            address = line[0].removeprefix("mem[")
            address = address.removesuffix("]")
            address = int(address)
            address = address | ormask
            floating_addresses = get_floating(address, volatile)
            for address in floating_addresses:
                mem[address] = value
    return mem


def get_floating(address, volatile):
    if len(volatile) == 1:
        return [address, address ^ (1 << volatile[0])]
    else:
        var = get_floating(address, volatile[1:])
        var.extend(get_floating(address ^ (1 << volatile[0]), volatile[1:]))
        return var


lp = loadprogram("dec14_input.txt")
# ans = execute1(l)
##print(ans)
# print(sum(ans.values()))
ans = execute2(lp)
print(ans)
print(sum(ans.values()))
a = 0b000000000000000000000000000000101010
