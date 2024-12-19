import copy


def next_pos(gdir, pos):
    i, j = pos
    if gdir == "i+1":
        return i + 1, j
    if gdir == "i-1":
        return i - 1, j
    if gdir == "j+1":
        return i, j + 1
    if gdir == "j-1":
        return i, j - 1


def change_direction(gdir):
    if gdir == "i+1":
        return "j-1"
    if gdir == "i-1":
        return "j+1"
    if gdir == "j+1":
        return "i+1"
    if gdir == "j-1":
        return "i-1"


def part1(lmap, R, C):

    directions = {"^": "i-1", "v": "i+1", ">": "j+1", "<": "j-1"}
    # find start pos and dir
    for i in range(R):
        for j in range(C):
            if lmap[i][j] in directions.keys():
                spos = (i, j)
                gdir = directions[lmap[i][j]]
                break
    print(spos, gdir)

    traversed_pos = set([spos])

    # setting initial state of guard
    guard = {"gdir": gdir, "pos": spos, "steps": 1}

    while (
        guard["pos"][0] >= 0
        and guard["pos"][1] >= 0
        and guard["pos"][0] < R
        and guard["pos"][1] < C
    ):

        npos = next_pos(guard["gdir"], guard["pos"])
        if npos[0] >= 0 and npos[1] >= 0 and npos[0] < R and npos[1] < C:

            if lmap[npos[0]][npos[1]] != "#":
                guard["pos"] = npos

                if guard["pos"] not in traversed_pos:
                    guard["steps"] += 1
                    traversed_pos.add(npos)
                    # traversed_j.add(npos[1])
                    # print(traversed_i)
                # else:
            else:
                guard["gdir"] = change_direction(guard["gdir"])
        else:
            break

    print(guard)
    print(f"part1 : {guard['steps']}")

    return traversed_pos, spos, gdir


def part2(opath, spos, gdir, lmap, R, C):

    new_obstacles = 0
    lmap_original = copy.deepcopy(lmap)  # lmap.copy()
    # removing start pos from possible pos
    opath.remove(spos)

    for ppos in opath:
        cur_loop = set()

        lmap[ppos[0]][ppos[1]] = "#"
        traversed_pos = set([spos])

        # setting initial state of guard
        guard = {"gdir": gdir, "pos": spos, "steps": 1}

        while (
            guard["pos"][0] >= 0
            and guard["pos"][1] >= 0
            and guard["pos"][0] < R
            and guard["pos"][1] < C
        ):

            npos = next_pos(guard["gdir"], guard["pos"])
            if npos[0] >= 0 and npos[1] >= 0 and npos[0] < R and npos[1] < C:

                if lmap[npos[0]][npos[1]] != "#":
                    guard["pos"] = npos

                    if guard["pos"] not in traversed_pos:
                        guard["steps"] += 1
                        traversed_pos.add(npos)
                        cur_loop = set()
                    else:
                        if guard["pos"] not in cur_loop:
                            cur_loop.add(guard["pos"])
                        else:
                            new_obstacles += 1
                            break
                else:
                    guard["gdir"] = change_direction(guard["gdir"])
            else:
                break

        lmap = copy.deepcopy(lmap_original)
    print(f"part2 : {new_obstacles}")


def main():

    lmap = []
    # with open("./day6_example.txt") as f:
    with open("./day6_input.txt") as f:
        lines = f.readlines()

    for line in lines:
        line = line.rstrip("\n")
        lmap.append(list(line))

    R = len(lmap)
    C = len(lmap[0])
    opath, spos, gdir = part1(lmap, R, C)
    part2(opath, spos, gdir, lmap, R, C)


if __name__ == "__main__":
    main()
