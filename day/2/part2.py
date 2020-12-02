with open ('input.txt', 'r') as file:
    split_lines = [i.split() for i in file.readlines()]

valid_passwords = 0

for line in split_lines:
    first_index, second_index = line[0].split('-')
    
    character = line[1].replace(':','')
    
    password = line[2]

    valid_first_index = password[int(first_index) - 1] == character
    valid_second_infex = password[int(second_index) - 1] == character

    #logical XOR
    if valid_first_index is not valid_second_infex:
        valid_passwords += 1


print(f'Valid passwords: {valid_passwords}')