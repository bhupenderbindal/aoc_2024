

def part1(list1, list2):
    list1.sort()
    list2.sort()
    
    abs_diff_list = []

    for i,_ in enumerate(list1):
        abs_diff_list.append(abs(list1[i] - list2[i]))

    print(sum(abs_diff_list))

def part2(list1, list2):

    dict_list2 = {}
    for item in list2:
        if item in dict_list2.keys():
            dict_list2[item] += 1
        else:
            dict_list2[item] = 1
    # print(dict_list2)

    sum_score = 0
    dict_keys = dict_list2.keys()
    for item in list1:
        if item in dict_keys:
            sum_score += item * dict_list2[item]

    print(sum_score)


def main():
    list1 = []
    list2 = []

    with open("./day1_input.txt") as f:
        lines = f.readlines()

    for line in lines:
        a, b = line.split('   ')
        b = b.rstrip('\n')
        list1.append(int(a))
        list2.append(int(b))
    
    print("Part 1:")
    part1(list1, list2)
    print("------------")
    print("Part 2:")
    part2(list1, list2)


if __name__ == "__main__":
    main()