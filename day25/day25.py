import sys


def smap(s):
    r = map((lambda x: "0" if x == "." else "1"), s)
    rr = int("".join(r))
    return rr


def part1(keys, locks):
    count = 0
    for lock, maxsum in locks:
        for key, _ in keys:
            matches = True
            for i in range(len(maxsum)):
                if int(key[i]) + int(lock[i]) <= int(maxsum[i]):
                    pass
                else:
                    matches = False
                    break

            if matches:
                count += 1

    print(f"count: {count}")


def main(filepath):
    with open(filepath) as f:
        lines = f.readlines()

    locks = []
    keys = []

    pattern = []
    for line in lines:
        if line == "\n":
            firststr = str(pattern[0])
            wf = len(firststr)
            laststr = str(pattern[-1])
            wl = len(laststr)

            if "0" not in firststr:

                valsum = sum(pattern[1:])
                l = len(str(valsum))
                if l < wf:
                    p = "0" * (wf - l) + str(valsum)
                else:
                    p = str(valsum)

                summax = str(len(pattern[1:-1])) * wf

                locks.append((p, summax))
                pattern = []

            if "0" not in laststr:

                valsum = sum(pattern[:-1])
                l = len(str(valsum))
                if l < wl:
                    p = "0" * (wl - l) + str(valsum)
                else:
                    p = str(valsum)

                summax = str(len(pattern[1:-1])) * wl

                keys.append((p, summax))
                pattern = []
        else:
            pattern.append(smap(line.rstrip("\n")))

    firststr = str(pattern[0])
    wf = len(firststr)
    laststr = str(pattern[-1])
    wl = len(laststr)

    if "0" not in firststr:

        valsum = sum(pattern[1:])
        l = len(str(valsum))
        if l < wf:
            p = "0" * (wf - l) + str(valsum)
        else:
            p = str(valsum)

        summax = str(len(pattern[1:-1])) * wf

        locks.append((p, summax))
        pattern = []

    if "0" not in laststr:

        valsum = sum(pattern[:-1])
        l = len(str(valsum))
        if l < wl:
            p = "0" * (wl - l) + str(valsum)
        else:
            p = str(valsum)

        summax = str(len(pattern[1:-1])) * wl

        keys.append((p, summax))
        pattern = []

    nkeys = len(keys)
    nlocks = len(locks)
    # print(nkeys, keys)
    # print(nlocks, locks)
    res1 = part1(keys, locks)
    # print(res1)


if __name__ == "__main__":
    args = sys.argv

    example_filepath = args[1]
    input_filepath = args[2]

    # main(example_filepath)
    main(input_filepath)
