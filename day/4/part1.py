required_keys = ['byr:','iyr:','eyr:','hgt:','hcl:','ecl:','pid:']

file = open('input.txt', 'r').readlines()  

passports = []
passport = ""

for line in file:
    if line == "\n":
        #add built p passport to list
        passports.append(passport)
        passport = ""
        continue

    #build up passport
    passport += line.replace('\n', ' ')

valid_passports = 0

for passport in passports:
        if all(key in passport for key in required_keys):
            valid_passports += 1
        else:
            print(f'Invalid passport: {passport}')

print(f'Valid passports: {valid_passports}')


