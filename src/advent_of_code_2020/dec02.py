# src/advent_of_code_2020/dec02.py


def loadpasswords(filename):
    with open(filename) as f:
        lines = f.readlines()
    pwds = []
    for line in lines:
        l = line.split()
        no = l[0].split("-")
        pwds.append((int(no[0]), int(no[1]), l[1].removesuffix(":"), l[2]))
    return pwds


def no_of_valid_pwds(pwd_list):
    valid = 0
    for pwd in pwd_list:
        if pwd[0] <= pwd[3].count(pwd[2]) <= pwd[1]:
            valid += 1
    return valid


def new_pwd_policy(pwd_list):
    valid = 0
    for pwd in pwd_list:
        chk = 0
        for ctrlchar in range(2):
            if pwd[3][pwd[ctrlchar] - 1] == pwd[2]:
                chk += 1
        valid += chk % 2
    return valid


l = loadpasswords("dec02_input.txt")
print(l)
print(no_of_valid_pwds(l))
print(new_pwd_policy(l))