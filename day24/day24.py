import sys
import operator


def solve(a, op, b):
    if op == "AND":
        return a & b
    elif op == "OR":
        return a | b
    elif op == "XOR":
        return operator.xor(a, b)
    else:
        print("invalid op exiting")
        exit(0)


def part1(processed, waiting):
    wdict = dict()
    initial_wires = processed.keys()

    # first iteration
    for a, op, b, out in waiting:
        if a in initial_wires and b in initial_wires:
            processed[out] = solve(processed[a], op, processed[b])
        else:
            if a in wdict.keys():
                wdict[a].append((op, b, out))
            else:
                wdict[a] = [(op, b, out)]

            if b in wdict.keys():
                wdict[b].append((op, a, out))
            else:
                wdict[b] = [(op, a, out)]

    # now process the wdict
    while len(wdict) != 0:
        for k, v in wdict.items():
            if k in processed.keys():
                for i, gate in enumerate(v):
                    if gate[1] in processed.keys():
                        processed[gate[2]] = solve(
                            processed[k], gate[0], processed[gate[1]]
                        )
                        v.pop(i)
        if v == []:
            wdict.pop(k)

    assert len(wdict) == 0
    print("-------------")

    ksorted = sorted(processed, reverse=True)
    rs = ""
    for kk in ksorted:
        if "z" in kk:
            rs += str(processed[kk])
    print(rs, int("0b" + rs, base=0))
    return int("0b" + rs, base=0)


def main(filepath):
    with open(filepath) as f:
        lines = f.readlines()

    processed = dict()
    waiting = []

    wires = True
    for line in lines:
        if line == "\n":
            wires = False
        else:
            if wires:
                a, b = line.rstrip("\n").split(":")
                b = int(b[1])
                processed[a] = b

            else:
                a, op, b, extra, out = line.rstrip("\n").split(" ")
                waiting.append((a, op, b, out))

    print(processed, waiting)
    res1 = part1(processed, waiting)
    print(res1)


if __name__ == "__main__":
    args = sys.argv

    example_filepath = args[1]
    input_filepath = args[2]

    # main(example_filepath)
    main(input_filepath)
