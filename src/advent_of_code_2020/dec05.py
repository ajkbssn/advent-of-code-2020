def seat_id(code):
    code = code.replace("B", "1")
    code = code.replace("F", "0")
    code = code.replace("R", "1")
    code = code.replace("L", "0")
    return int(code, 2)


def loadboardingpass(filename):
    with open(filename, "r") as f:
        lines = f.readlines()
    return [line.strip() for line in lines]


def return_empty(s):
    if len(s) == 2:
        return s
    half = len(s) // 2
    if s[half - 1] - s[0] == half:
        return return_empty(s[:half])
    else:
        return return_empty(s[half:])


s = [seat_id(line) for line in loadboardingpass("dec05_input.txt")]
s.sort()
print([ele for ele in range(max(s) + 1) if ele not in s])
