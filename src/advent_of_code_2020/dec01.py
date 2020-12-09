# src/advent_of_code_2020/dec01.py

def loadnumbers(filename):
    with open(filename) as f:
        lines = f.readlines()
    return [int(line) for line in lines]


def find_two_integers(integerlist,targetsum):
    for i, integer in enumerate(integerlist):
        if targetsum-integer in integerlist[i+1:]:
            return integer, targetsum-integer,i
    return false            
