import sys
from copy import deepcopy


def find_triplet(conn_list):

    triplet_dict = dict()

    for i, coni in enumerate(conn_list):
        for j, conj in enumerate(conn_list):
            if i != j:
                if coni.isdisjoint(conj):
                    pass
                else:
                    tri = ",".join(sorted(coni.union(conj)))
                    if tri in triplet_dict.keys():
                        triplet_dict[tri] += 1
                    else:
                        triplet_dict[tri] = 1

    triplet_dict_final = dict()
    count = 0
    for k, v in triplet_dict.items():
        if v == 6:
            triplet_dict_final[k] = v
            if k[0] == "t" or k[3] == "t" or k[6] == "t":
                count += 1

    print(triplet_dict_final, len(triplet_dict_final), count)


def part1(conn_list):
    find_triplet(conn_list)


def main(filepath):
    with open(filepath) as f:
        lines = f.readlines()

    conn_list = []
    for line in lines:
        conn_list.append(set((line.rstrip("\n")).split("-")))

    N = len(conn_list)
    print(conn_list, N)
    res1 = part1(conn_list)
    # print(res1)


if __name__ == "__main__":
    args = sys.argv

    example_filepath = args[1]
    input_filepath = args[2]

    # main(example_filepath)
    main(input_filepath)
