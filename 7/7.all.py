import re

def traverse(rules, target, bags):
    for key in rules.keys():
        for subkey in rules[key]:
            if (target in subkey) and (key not in bags):
                bags.append(key)
    return bags

def tally(rules, target):
    bags = []
    for subkey in rules[target]:
        tokens = subkey.split(' ', 1)
        newkey = re.split(r'bags?', tokens[1])[0].strip()
        if 'no' in newkey:
            bags += [None]
        else:
            bags += [newkey] * int(tokens[0])
    return bags             

with open('input.txt', 'r') as f:
    lines = f.read().split('\n')
    rules = dict(line.split(' bags contain ') for line in lines)
    for key in rules.keys():
        subkeys = []
        val = rules[key]
        while True:
            match = re.search(r'\d* \w* \w* bags?', val)
            if match:
                text = match.group()
                subkeys.append(text)
                val = val[match.span()[1]:]
            else:
                break
        rules[key] = subkeys

    # part 1

    target = "shiny gold"
    bags = []
    bags = traverse(rules, target, bags) # seed the open nodes
    bags_iter = bags[:]
    while True:
        before_bags_count = len(bags)
        for target in bags_iter:
            bags = traverse(rules, target, bags)
        after_bags_count = len(bags)
        if after_bags_count == before_bags_count:
            break
        bags_iter = bags[:]
    print(len(bags))

    # part 2

    target = 'shiny gold'
    bags = tally(rules, target) # seed the open nodes
    bags_iter = bags[:]
    ptr = 0
    while True:
        new_ptr = len(bags)
        for target in bags_iter[ptr:]:
            new_bags = tally(rules, target)
            bags += new_bags
        if ptr == len(bags):
            break
        bags_iter = bags[:]
        ptr = new_ptr
    bags = bags[:ptr]
    print(len(bags))