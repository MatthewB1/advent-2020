with open ('input.txt', 'r') as file:
    split_lines = [i.split() for i in file.readlines()]

valid_passwords = 0

for line in split_lines:
    lower, upper = line[0].split('-')
    
    character = line[1].replace(':','')
    
    password = line[2]

    count = password.count(character)
 
    if int(lower) <= count and count <= int(upper):
        valid_passwords += 1

print(f'Valid passwords: {valid_passwords}')