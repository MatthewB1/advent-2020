file = open('input.txt', 'r').read()

forms = file.split('\n\n')

common_answers = []

for form in forms:
    rows = [(set(row)) for row in form.split('\n')]
    #intersects all sets in a list, creates list of common elements
    common_answers.append(rows[0].intersection(*rows))

length = sum(len(row) for row in common_answers)

print(length)


