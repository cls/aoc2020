import re
import sys

pattern = re.compile(r'(\S+):(\S+)')

def read_passports(lines):
    passport = {}
    for line in lines:
        line = line.strip()
        if line:
            for match in pattern.finditer(line):
                passport[match.group(1)] = match.group(2)
        elif passport:
            yield passport
            passport.clear()
    if passport:
        yield passport

requirements = {
    'byr': re.compile(r'19[2-9][0-9]|200[0-2]'),
    'iyr': re.compile(r'201[0-9]|2020'),
    'eyr': re.compile(r'202[0-9]|2030'),
    'hgt': re.compile(r'(1[5-8][0-9]|19[0-3])cm|(59|6[0-9]|7[0-6])in'),
    'hcl': re.compile(r'#[0-9a-f]{6}'),
    'ecl': re.compile(r'amb|blu|brn|gry|grn|hzl|oth'),
    'pid': re.compile(r'[0-9]{9}'),
}

required_keys = requirements.keys()

valid1 = 0
valid2 = 0

for passport in read_passports(sys.stdin):
    if required_keys & passport.keys() == required_keys:
        valid1 += 1
        for key, requirement in requirements.items():
            if not requirement.fullmatch(passport[key]):
                break
        else:
            valid2 += 1

print(valid1)
print(valid2)
