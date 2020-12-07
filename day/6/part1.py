file = open('input.txt', 'r').read()

forms = [set(i.replace('\n', '')) for i in file.split('\n\n')]

length = sum(len(form) for form in forms)

print(f'Total count of \'yes\' answers: {length}')


#one line version
# print("Yes answers:", sum(len(form) for form in [set(i.replace('\n', '')) for i in open('input.txt', 'r').read().split('\n\n')]))