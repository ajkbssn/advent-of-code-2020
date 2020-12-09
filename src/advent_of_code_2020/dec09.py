# /src/advent_of_code/dec09.py


def loadnumbers(filename):
    with open(filename) as f:
        lines = f.readlines()
    return [int(line) for line in lines]


def allowed(numberlist):
    ok = []
    for i, elem_i in enumerate(numberlist):
        for elem_j in numberlist[i + 1 :]:
            if elem_i + elem_j not in ok:
                ok.append(elem_i + elem_j)
    return ok


def first(numberlist, preamblelength):
    if len(numberlist) < preamblelength:
        return False, None, None
    index = preamblelength - 1
    cont = True
    while cont:
        index += 1
        if index == len(numberlist):
            return False, None
        cont = numberlist[index] in allowed(numberlist[index - preamblelength : index])
    return True, numberlist[index], index


def contiguousset(numberlist, invalidnumber):
    start = 0
    end = start + 1
    setsum = sum(numberlist[start : end + 1])
    done = setsum == invalidnumber
    while not done:
        while setsum < invalidnumber:
            end += 1
            if end == len(numberlist):
                return False
            setsum += numberlist[end]
        while setsum > invalidnumber:
            setsum -= numberlist[start]
            start += 1
        done = setsum == invalidnumber

    return numberlist[start : end + 1]


def answer(filename, preamblelength):
    n = loadnumbers(filename)
    chk1, outlier, chk2 = first(n, preamblelength)
    numberlist = contiguousset(n, outlier)
    return max(numberlist) + min(numberlist)
