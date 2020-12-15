# src/
import re

passport_fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]


def loadpassports(filename):
    with open(filename) as f:
        lines = f.readlines()
    passports = []

    line_no = 0
    while line_no < len(lines):
        next_passport = False
        passport = {}
        while not next_passport and line_no < len(lines):
            items = lines[line_no].split()
            if len(items) == 0:
                next_passport = True
            else:
                for item in items:
                    temp = item.split(":")
                    passport[temp[0]] = temp[1]
            line_no += 1
        passports.append(passport)
    return passports


def _valid_passport(passport):
    for field in passport_fields:
        if field not in passport:
            return False
    return True


def valid_passport(passport):
    # Validate mandatory fields

    if not _valid_passport(passport):
        return False

    # Validate numerical
    if not (1920 <= int(passport["byr"]) <= 2002):
        return False
    if not (2010 <= int(passport["iyr"]) <= 2020):
        return False
    if not (2020 <= int(passport["eyr"]) <= 2030):
        return False

    # Validate Height
    if "cm" in passport["hgt"] and not (150 <= int(passport["hgt"][:-2]) <= 193):
        return False
    elif "in" in passport["hgt"] and not (59 <= int(passport["hgt"][:-2]) <= 76):
        return False
    if "cm" not in passport["hgt"] and "in" not in passport["hgt"]:
        return False

    # Validate strings/enums
    if passport["ecl"] not in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
        return False
    if re.match(r"^\#[0-9a-f]{6}$", passport["hcl"]) is None:
        return False
    if re.match(r"^\d{9}$", passport["pid"]) is None:
        return False

    return True


d = loadpassports("dec04_input.txt")
valid = 0
for p in d:
    if valid_passport(p):
        valid += 1
print(valid)