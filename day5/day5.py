

def rules_to_dict(rules):
    rules_dict = {}
    for rule in rules:
        k,v = rule[0], rule[1]
        if k in rules_dict.keys():
            rules_dict[k].append(v)
        else:
            rules_dict[k] = [v]
    
    return rules_dict

def part1(rules, updates):
    rules_dict = rules_to_dict(rules)
    updates_passed = []
    updates_failed = []

    for update in updates:
        
        for i, _ in enumerate(update[:-1]):
            elem = update[i]
            remaining_elem = update[i+1:]
            if elem in rules_dict.keys():
                for item in remaining_elem:
                    if item in rules_dict[elem]:
                        rules_passed = True
                    else:
                        rules_passed = False
                        break        
            else:
                rules_passed = False
                break
            if rules_passed:
                print(elem)
            else:
                break
        
        if rules_passed:
            updates_passed.append(update)
        else:
            updates_failed.append(update)

    sum = 0
    for update in updates_passed:
        l = len(update)
        if l%2 == 0:
            print(f"even sized update {update}")
        else:
            sum += update[int(l/2)]
    print(sum)

    return sum, updates_failed


def part2(rules, updates_failed):
    rules_dict = rules_to_dict(rules)
    for update in updates_failed:
        rules_passed = False
    
        while not rules_passed:
            for i, _ in enumerate(update[:-1]):
                elem = update[i]
                remaining_elem = update[i+1:]
                if elem in rules_dict.keys():
                    for rem_elem in remaining_elem:
                        if rem_elem in rules_dict[elem]:
                            rules_passed = True
                        else:
                            rules_passed = False
                            ind_a = i 
                            ind_b = update.index(rem_elem)
                            update[ind_a] = rem_elem
                            update[ind_b] = elem

                            break        
                else: # ie this item is not greater than any elem, so shift at the end
                    rules_passed = False
                    movetoend = update.pop(update.index(elem))
                    update.append(movetoend)
                    break
                if rules_passed:
                    pass
                else:
                    break
        
    sum = 0
    for update in updates_failed:
        l = len(update)
        if l%2 == 0:
            print(f"even sized update {update}")
        else:
            sum += update[int(l/2)]
    print(sum)


def main():

    rules = []
    updates =[]

    # with open("./day5_example.txt") as f:
    with open("./day5_input.txt") as f:
        lines = f.readlines()

    rule_flag = True
    for line in lines:
        if line == "\n":
            rule_flag = False
        else:
            line = line.rstrip('\n')
            if rule_flag:
                line = [int(i) for i in line.split('|')]
                rules.append(line)
            else:
                line = [int(i) for i in line.split(',')]
                updates.append(line)
                
    # print(rules)
    # print(updates) 
    res_part1, updates_failed = part1(rules, updates)
    part2(rules, updates_failed)
        

if __name__ == "__main__":
    main()