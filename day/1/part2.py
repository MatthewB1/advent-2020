with open ('input.txt', 'r') as file:
    expenses = [int(i) for i in file.readlines()]

size = len(expenses)

for i in range(0, size):
    for j in range(i, size):
        for k in range(j, size):
            if expenses[i] + expenses[j] + expenses[k] == 2020:
                print(f"Answer: {expenses[i]*expenses[j]*expenses[k]}")
                break