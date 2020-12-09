# src/advent_of_code_2020/dec01.py

def loadnumbers(filename):
    with open(filename) as f:
        lines = f.readlines()
    return [int(line) for line in lines]


def find_two_integers(integerlist,targetsum):
    i=0
    while i < len(integerlist)-1:
        tmp=integerlist[i]
        if targetsum-tmp in integerlist[i+1:]:
            return tmp, targetsum-tmp, i
        i +=1
    return false            
