with open ('input.txt', 'r') as file:
    expenses = [int(i) for i in file.readlines()]

size = len(expenses)

for i in range(0, size):
    for j in range(i, size):
        if expenses[i] + expenses[j] == 2020:
            print(f"Answer: {expenses[i]*expenses[j]}")
            break