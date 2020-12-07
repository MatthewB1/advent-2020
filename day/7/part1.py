file = open('input.txt', 'r')
lines = [list(i.replace('bags', 'bag').split(' contain ')) for i in file.readlines()]

rules = {}

for line in lines:
    key = line[0]
    val = ''.join([i for i in line[1] if not i.isdigit()]).replace('.\n','').strip()
    rules[key] = val

can_contain_gold = []

def find_can_contain(bags):
    next_bags = []

    for bag in bags:
        for key, val in rules.items():
            if bag in val:
                print(f'found {bag} in {key} : {val}')
                can_contain_gold.append(key)
                next_bags.append(key)
    
    if len(next_bags) == 0:
        return can_contain_gold

    return find_can_contain(next_bags)

shiny_gold_count = len(set(find_can_contain(['shiny gold bag'])))

print(f'Total amount of bags that can contain shiny gold: {shiny_gold_count}')