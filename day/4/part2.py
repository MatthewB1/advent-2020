import re as regex

required_keys = ['byr:','iyr:','eyr:','hgt:','hcl:','ecl:','pid:']

valid_ecls = ['amb','blu','brn','gry','grn','hzl','oth']

def validate_height(height):
    if 'cm' in height:
        return 150 <= int(height.replace('cm','')) <= 193
    if 'in' in height:
        return 59 <= int(height.replace('in','')) <= 76

validators = {
    "byr" : lambda byr: len(byr) == 4 and 1920 <= int(byr) <= 2002,
    "iyr" : lambda iyr: len(iyr) == 4 and 2010 <= int(iyr) <= 2020,
    "eyr" : lambda eyr: len (eyr) == 4 and 2020 <= int(eyr) <= 2030,
    "hgt" : lambda hgt: validate_height(hgt),
    "hcl" : lambda hcl: regex.search(r'^#(?:[0-9a-fA-F]{3}){1,2}$', hcl),
    "ecl" : lambda ecl: ecl in valid_ecls,
    "pid" : lambda pid: len(pid) == 9 and pid.isdigit(),
    "cid" : lambda cid: True
}

def validate_keys(passport):    
    for keyval in passport.split(' '):
        if keyval == '':
            continue    

        try:
            key, val = keyval.split(':')
        except: 
            print(f'Invalid keyval: {keyval}')
            return False

        if not validators[key](val):
            print(f'Keyval {keyval} is invalid.')
            return False

    return True


file = open('input.txt', 'r').readlines()

passports = []

passport = ""

for line in file:
    if line == "\n":
        #add built up passport to list
        passports.append(passport)
        passport = ""
        continue

    #build up passport
    passport += line.replace('\n', ' ')

valid_passports = 0

for passport in passports:
        if all(key in passport for key in required_keys) and validate_keys(passport):
            valid_passports += 1
        else:
            print(f'Invalid passport: {passport}\n')

print(f'Valid passports: {valid_passports}')