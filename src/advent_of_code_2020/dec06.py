def loadcustomsforms(filename):
    with open(filename, "r") as f:
        lines = f.readlines()

    allforms = []
    groupforms = []

    for line in lines:
        if len(line.strip()) == 0:
            allforms.append(groupforms)
            groupforms = []
        else:
            groupforms.append(line.strip())
    if len(groupforms) > 0:
        allforms.append(groupforms)

    return allforms


def makedicts(allforms):
    dicts = []
    for group in allforms:
        groupforms = {"size": 0}
        for form in group:
            groupforms["size"] += 1
            for flag in form:
                if flag in groupforms:
                    groupforms[flag] += 1
                else:
                    groupforms[flag] = 1
        dicts.append(groupforms)
    return dicts


def countyes(dicts):
    n = 0
    for d in dicts:
        n += len(d) - 1
    return n


def countallyes(dicts):
    n = 0
    for d in dicts:
        for k in d:
            if k != "size":
                if d[k] == d["size"]:
                    n += 1
    return n


l = loadcustomsforms("dec06_input.txt")
d = makedicts(l)
s = countallyes(d)
print(s)
