from functools import cache


# this cache is little useful for the solution
@cache
def rule_map3(x):
    # rules in priority order
    if x == 0:
        return [1]
    elif len(str(x)) % 2 == 0:
        sx = str(x)
        l = len(sx)
        return [int(sx[0 : int(l / 2)]), int(sx[int(l / 2) :])]
    else:
        return [x * 2024]


def part2(inp_arr, n):

    fdict = dict()

    # create first base dict
    for item in inp_arr:
        tarr = rule_map3(item)
        # tarr has 1 or two ele
        for x in tarr:
            if x in fdict.keys():
                fdict[x] += 1
            else:
                fdict[x] = 1
    print(fdict)

    # iterate over for remaining times
    for _ in range(n - 1):
        newdict = dict()
        for k, v in fdict.items():
            tarr = rule_map3(k)
            # tarr has 1 or two ele
            for x in tarr:
                if x in newdict.keys():
                    newdict[x] += 1 * v
                else:
                    newdict[x] = 1 * v
        fdict = newdict

    return sum(newdict.values())


# falls victim to exponential increase in array size
def part1(inp_arr, n):
    old_arr = inp_arr

    for _ in range(n):
        new_arr = []
        for item in old_arr:
            new_arr.extend(rule_map3(item))
        old_arr = new_arr

    return len(new_arr)


def main():

    # with open("./day11_example.txt") as f:
    with open("./day11_input.txt") as f:
        lines = f.readlines()

    line = lines[0].rstrip("\n").split(" ")
    inp_arr = [int(i) for i in line]
    # print(inp_arr)

    # num of blinks
    n = 25

    res1 = part1(inp_arr, n)
    print(f"res1 without hashmap = {res1}")

    # as the number of items remain less it becomes item->frequency
    res2 = part2(inp_arr, n)
    print(f"res1 = {res2}")

    n = 75

    res2 = part2(inp_arr, n)
    print(f"res2 = {res2}")


if __name__ == "__main__":
    main()
