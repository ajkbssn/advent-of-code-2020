# src/advent_of_code_2020/dec08.py


def loadprogram(filename):
    with open(filename) as f:
        lines = f.readlines()
    pgmdict = {}
    for i, line in enumerate(lines):
        instruction = line.split()
        pgmdict[i] = [instruction, []]
    return pgmdict


def exe_next(pgmdict, next, acc, seq):
    pgmdict[next][1].append(seq)
    if pgmdict[next][0][0] == "acc":
        acc += int(pgmdict[next][0][1])
        next += 1
    elif pgmdict[next][0][0] == "nop":
        next += 1
    else:
        next += int(pgmdict[next][0][1])
    seq += 1
    return next, acc, seq


def return_acc_before_2nd_run(pgmdict):
    done = False
    new_acc = 0
    new_seq = 0
    new_next = 0
    while not done:
        acc, seq, next = new_acc, new_seq, new_next
        new_next, new_acc, new_seq = exe_next(pgmdict, next, acc, seq)
        done = (new_next == len(pgmdict)) or (len(pgmdict[new_next][1]) == 1)
    return next, acc, seq


def clear_pgm_dict(pgmdict):
    for key in pgmdict:
        pgmdict[key][1] = []


def possible_changes(used_pgmdict):
    possible_changes_list = []
    for key in used_pgmdict:
        if len(used_pgmdict[key][1]) > 0:
            if used_pgmdict[key][0][0] == "nop":
                steps = int(used_pgmdict[key][0][1])
                if len(used_pgmdict[key + steps][1]) == 0:
                    possible_changes_list.append(key)
            elif used_pgmdict[key][0][0] == "jmp":
                if len(used_pgmdict[key + 1][1]) == 0:
                    possible_changes_list.append(key)
            else:
                pass
    return possible_changes_list


def main(fname):
    d1 = loadprogram(fname)
    return_acc_before_2nd_run(d1)
    test_list = possible_changes(d1)
    test_list.sort(reverse=True)
    print(len(test_list))
    print(test_list)
    done = False
    i = 0
    while not done:
        d2 = d1.copy()
        clear_pgm_dict(d2)
        if d2[test_list[i]][0][0] == "jmp":
            d2[test_list[i]][0][0] = "nop"
        else:
            d2[test_list[i]][0][0] = "jmp"
        next, acc, seq = return_acc_before_2nd_run(d2)
        done = len(d2) - 1 == next
        i += 1
    print(i, next, acc, seq)


main("dec08_input.txt")