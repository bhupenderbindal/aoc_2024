def find_all_mul(s):
    all_mul_str = []

    while len(s) != 0:
        try:
            i = s.index("mul(")
        except ValueError as e:
            print("no 'mul('  found exiting")
            break
        all_mul_str.append(s[i:])
        s = s[i + 4 :]
    return all_mul_str


def find_all_xs(s, x):
    all_mul_str = []
    while len(s) != 0:
        try:
            i = s.index(x)
        except ValueError as e:
            print(f"no {x}  found exiting")
            break
        all_mul_str.append(s[i:])
        s = s[i + 4 :]
    return all_mul_str


def find_mullwithend(s):
    try:
        i = s.index(")")
        mulend = s[: i + 1]
        # print(mulend)
        return mulend
    except ValueError as e:
        print("no closing bracket found, exiting")


def is_int(s):
    for i in s:
        if i not in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            return None
    return int(s)


def find_ints(s):
    # trim mul(
    i = s.index("mul(")
    s = s[i + 4 :]
    # trim )
    i = s.index(")")
    s = s[:i]

    try:
        splits = s.split(",")
        if len(splits) != 2:
            print("more than 1 comma")
        else:
            s1 = splits[0]
            s2 = splits[1]
            i1 = is_int(s1)
            if i1:
                print(f"s1 is int: {i1}")
            else:
                return None

            i2 = is_int(s2)
            if i2:
                print(f"s2 is int: {i2}")
            else:
                return None

            m = i1 * i2
            return m

    except Error as e:
        print("split by comma error, exiting")


def part1(istr):
    sum = 0

    all_mul_str = find_all_mul(istr)
    for mulstr in all_mul_str:
        # print(f"step1: {mulstr}")
        mullwithend = find_mullwithend(mulstr)
        if mullwithend:
            # print(f"step2: {mullwithend}")
            sumofints = find_ints(mullwithend)
            if sumofints:
                sum += sumofints

    print(f"part 1 : {sum}")
    return sum


def part2(istr):
    s2 = 0
    istr = "do()" + istr

    do_strs = find_all_xs(istr, x="do()")
    print(do_strs)
    # for every do() string we need to find first dont() string if exists
    # and extract the part between them
    for dostr in do_strs:
        try:
            i = dostr.index("don't()")
            s = dostr[:i]
        except ValueError as e:
            print(f"no don't()  found exiting")
            s = dostr

        # stripping the do()
        s = s[4:]
        # each do() can have multiple do() which causes repetition so we extract before next do to avoid this
        try:
            i = s.index("do()")
            s = s[:i]
        except ValueError as e:
            print(f"no other do() found exiting")
            # s = dostr

        # for the part extracted we calculate the mul from part1
        s2 += part1(s)

    print(s2)


def main():

    # with open("./day3_example.txt") as f:
    with open("./day3_input.txt") as f:
        lines = f.readlines()

    istr = ""
    # input is a single, so should be a single string
    for line in lines:
        istr += line
    # istr = lines
    print(istr)
    part1(istr)
    # part2(istr)


if __name__ == "__main__":
    main()
