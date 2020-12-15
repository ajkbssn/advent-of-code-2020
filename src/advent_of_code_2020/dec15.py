starts = [[0, 3, 6], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [6, 13, 1, 15, 2, 0]]
stop = 30000000

for st in starts:
    turn = len(st)
    dict = {}
    init = 1
    while init < turn:
        dict[st[init - 1]] = init
        init += 1
    last = st[-1]
    while turn < stop:
        if last in dict:
            tmp = turn - dict[last]
            dict[last] = turn
            last = tmp
        else:
            dict[last] = turn
            last = 0
        turn += 1
    print(last, turn)
