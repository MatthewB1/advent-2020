file = open('input.txt', 'r')
lines = [list(i.replace('bags', 'bag').split(' contain ')) for i in file.readlines()]

rules = {}
        
for line in lines:
    key = line[0]
    val = line[1].replace('.\n','').strip()
    rules[key] = val


def split_rule_val(rule_val):
    bag_counts = []
    bags = [i.strip() for i in rule_val.split(',')]
    for bag in bags:
        if "no other bag" in bag:
            continue
        key = ''.join([i for i in bag if i.isdigit()]).strip()
        val = ''.join([i for i in bag if not i.isdigit()]).strip()
        bag_counts.append((int(key), val))
    
    return(bag_counts)
 

def count_containing_bags(bag):
    contained_bags = split_rule_val(rules[bag])

    if len(contained_bags) == 0:
        return 0

    return sum(key + key * count_containing_bags(val) for (key, val) in contained_bags)


count = count_containing_bags('shiny gold bag')

print(f'Total bags held by shiny gold bag: {count}')