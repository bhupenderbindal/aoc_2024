import sys
import operator as op


def mix(sn, n):

    r1 = op.xor(sn, n)
    return r1


def prune(sn):
    r2 = sn % 16777216
    return r2


def f1(n):
    n1 = n * 64
    # mix
    n2 = mix(n, n1)
    # prune
    n3 = prune(n2)
    return n3


def f2(n):
    n1 = int(n / 32)
    # mix
    n2 = mix(n, n1)
    # prune
    n3 = prune(n2)
    return n3


def f3(n):
    n1 = n * 2048
    # mix
    n2 = mix(n, n1)
    # prune
    n3 = prune(n2)
    return n3


def part1(all_sec_num, N, repeat):
    res_dict = dict()
    for sn in all_sec_num:
        sn_old = sn
        for _ in range(repeat):
            sn_new = f3(f2(f1(sn_old)))
            sn_old = sn_new
        res_dict[sn] = sn_new

    # pp(res_dict)
    res1 = sum(res_dict.values())
    return res1


def main(filepath):
    with open(filepath) as f:
        lines = f.readlines()

    all_sec_num = []
    for line in lines:
        all_sec_num.append(int(line.rstrip("\n")))

    N = len(all_sec_num)
    print(all_sec_num, N)
    res1 = part1(all_sec_num, N, repeat=2000)
    print(res1)


if __name__ == "__main__":
    args = sys.argv

    example_filepath = args[1]
    input_filepath = args[2]

    # main(example_filepath)
    main(input_filepath)

    # print(mix(42, 15))
    # print(prune(100000000))

    # example 123
    # r1 = f1(123)
    # r2 = f2(r1)
    # r3 = f3(r2)
    # print(r1,r2, r3)
