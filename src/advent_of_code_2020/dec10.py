# src/advent_of_code_2020/dec10.py


def loadnumbers(filename):
    with open(filename) as f:
        lines = f.readlines()
    return [int(line) for line in lines]


def difflist(numberlist):
    n = numberlist.copy()
    n.sort()
    n.insert(0, 0)
    return [n[i] - n[i - 1] for i in range(1, len(n))]


def calc3sand1s(numberlist):
    n = numberlist.copy()
    n.sort()
    n.insert(0, 0)
    n.append(n[-1] + 3)
    d = {}
    diff_list = [n[i] - n[i - 1] for i in range(1, len(n))]
    for i in diff_list:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    return d


def recursive_countcombos(start, sorted_available_adapaters):
    ways = 0
    working_copy = sorted_available_adapaters.copy()
    if len(working_copy) == 1:
        ways += 1
    if len(working_copy) > 1 and working_copy[0] - start < 4:
        ways += recursive_countcombos(working_copy[0], working_copy[1:])
    if len(working_copy) > 2 and working_copy[1] - start < 4:
        ways += recursive_countcombos(working_copy[1], working_copy[2:])
    if len(working_copy) > 3 and working_copy[2] - start < 4:
        ways += recursive_countcombos(working_copy[2], working_copy[3:])
    return ways


def countcombos(alist):
    alistcopy = alist.copy()
    alistcopy.sort()
    return recursive_countcombos(0, alistcopy)


def ways_to_go(alist):
    dlist = difflist(alist)
    w = []
    length = len(dlist)
    for i, d in enumerate(dlist):
        temp = 1
        if (length > i + 2) and (sum(dlist[i + 1 : i + 3]) < 4):
            temp += 1
        if (length > i + 3) and (sum(dlist[i + 1 : i + 4]) < 4):
            temp += 1
        w.append(temp)
    return w


def count(wtg_list):
    tmp = wtg_list.copy()
    dict = {}
    dict[0] = 1
    for i, elem in enumerate(tmp):
        for j in range(elem):
            if (i + j + 1) in dict:
                dict[i + j + 1] += dict[i]
            else:
                dict[i + j + 1] = dict[i]
    return dict[len(dict) - 1], dict


def graphdict(adapterlist):
    alist = adapterlist.copy()
    alist.sort()
    alist.insert(0, 0)
    gdict = {}
    for a in alist:
        gdict[a] = 0
    gdict[0] = 1
    for a in alist:
        for j in range(1, 4):
            if (a + j) in gdict:
                gdict[a + j] += gdict[a]
    return gdict


ab = [16, 10, 15, 5, 1, 11, 7, 19, 6, 12, 4]
# b = 0
# assert countcombos(0, a) == 8
abc = graphdict(ab)
l = loadnumbers("dec10_test.txt")
lc = l.copy()
print(lc.sort())
# d = difflist(l)
# print(d)
wtg = ways_to_go(l)
print(wtg)
X, xd = count(wtg)
print(X)
print(countcombos(l))
print(graphdict(l))
