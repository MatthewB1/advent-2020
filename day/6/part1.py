file = open('input.txt', 'r').read()

forms = [set(i.replace('\n', '')) for i in file.split('\n\n')]

length = sum(len(form) for form in forms)

print(f'Total count of \'yes\' answers: {length}')