def map_to_dict_plot(imap):
    dict_plot = {}

    for i, row in enumerate(imap):
        for j, ch in enumerate(row):
            if ch in dict_plot.keys():
                dict_plot[ch].append((i, j))
            else:
                dict_plot[ch] = [(i, j)]

    for key, val in dict_plot.items():
        dict_plot[key] = sorted(val)

    return dict_plot


def check_coord_in_regs(coord, reg_dict, H, W, all_coord, founds):
    found = False

    ii, jj = coord[0], coord[1]
    directions = []
    directions.append((ii, jj))
    directions.append((ii + 1, jj))  # down
    directions.append((ii - 1, jj))  # up
    directions.append((ii, jj + 1))  # right
    directions.append((ii, jj - 1))  # left

    neigbors = []

    for i, j in directions:
        if i >= 0 and j >= 0 and i < H and j < W:
            if (i, j) in all_coord:
                neigbors.append((i, j))
                # neigbors_ind.append(all_coord.index((i,j)))
                founds[all_coord.index((i, j))] = 1

    for reg, rcoords in reg_dict.items():
        for a, b in rcoords:

            for neig in neigbors:
                if abs(neig[0] - a) + abs(neig[1] - b) <= 1:
                    found = True
                    return reg, neigbors, founds

    if not found:
        return None, neigbors, founds


def calc_per(k, v, imap, H, W):
    reg = k[0]
    per = 0

    for ii, jj in v:
        directions = []
        directions.append((ii + 1, jj))  # down
        directions.append((ii - 1, jj))  # up
        directions.append((ii, jj + 1))  # right
        directions.append((ii, jj - 1))  # left

        for i, j in directions:
            if i >= 0 and j >= 0 and i < H and j < W:
                if imap[i][j] == reg:
                    pass
                else:
                    per += 1
            else:
                per += 1

    return per


def calc_per2(k, v, imap, H, W):
    reg = k[0]
    per = 0

    b_left, b_right, b_up, b_down = dict(), dict(), dict(), dict()

    for ii, jj in v:

        # down
        i, j = (ii + 1, jj)

        if i >= 0 and j >= 0 and i < H and j < W:
            if imap[i][j] == reg:
                pass
            else:
                if i in b_down.keys():
                    b_down[i].append(j)
                else:
                    b_down[i] = [j]
        else:
            if i in b_down.keys():
                b_down[i].append(j)
            else:
                b_down[i] = [j]

        # up
        i, j = (ii - 1, jj)
        if i >= 0 and j >= 0 and i < H and j < W:
            if imap[i][j] == reg:
                pass
            else:
                if i in b_up.keys():
                    b_up[i].append(j)
                else:
                    b_up[i] = [j]
        else:
            if i in b_up.keys():
                b_up[i].append(j)
            else:
                b_up[i] = [j]

        # right
        i, j = (ii, jj + 1)
        if i >= 0 and j >= 0 and i < H and j < W:
            if imap[i][j] == reg:
                pass
            else:
                if j in b_right.keys():
                    b_right[j].append(i)
                else:
                    b_right[j] = [i]
        else:
            if j in b_right.keys():
                b_right[j].append(i)
            else:
                b_right[j] = [i]

        # left
        i, j = (ii, jj - 1)
        if i >= 0 and j >= 0 and i < H and j < W:
            if imap[i][j] == reg:
                pass
            else:
                if j in b_left.keys():
                    b_left[j].append(i)
                else:
                    b_left[j] = [i]
        else:
            if j in b_left.keys():
                b_left[j].append(i)
            else:
                b_left[j] = [i]

    per = 0
    for b in [b_left, b_right, b_up, b_down]:
        per += calc_bound_segments(b)

    return per


def calc_bound_segments(bound):

    tot_seg = 0
    for loc, line in bound.items():
        line = sorted(line)
        seg = 1
        for i in range(len(line) - 1):
            if line[i + 1] - line[i] == 1:
                pass
            else:
                seg += 1
        tot_seg += seg

    return tot_seg


class crawler:

    def __init__(self, H, W, val, founds):
        self.founds = founds
        self.val = val
        self.path = set()

    def crawl(self, coord):
        ii, jj = coord
        self.founds.add((ii, jj))
        self.path.add((ii, jj))
        if (ii + 1, jj) in self.val and (ii + 1, jj) not in self.founds:
            self.crawl((ii + 1, jj))
        if (ii - 1, jj) in self.val and (ii - 1, jj) not in self.founds:
            # self.founds.add((ii, jj))
            self.crawl((ii - 1, jj))
        if (ii, jj + 1) in self.val and (ii, jj + 1) not in self.founds:
            # self.founds.add((ii, jj))
            self.crawl((ii, jj + 1))
        if (ii, jj - 1) in self.val and (ii, jj - 1) not in self.founds:
            # self.founds.add((ii, jj))
            self.crawl((ii, jj - 1))

    def crawl2(self, coord):
        ii, jj = coord
        self.founds.add((ii, jj))
        self.path.add((ii, jj))
        if (ii + 1, jj) in self.val and (ii + 1, jj) not in self.founds:
            self.crawl((ii + 1, jj))
        if (ii - 1, jj) in self.val and (ii - 1, jj) not in self.founds:
            # self.founds.add((ii, jj))
            self.crawl((ii - 1, jj))
        if (ii, jj + 1) in self.val and (ii, jj + 1) not in self.founds:
            # self.founds.add((ii, jj))
            self.crawl((ii, jj + 1))
        if (ii, jj - 1) in self.val and (ii, jj - 1) not in self.founds:
            # self.founds.add((ii, jj))
            self.crawl((ii, jj - 1))


def coord_to_region(key, val, H, W):
    reg_num = 0
    reg_dict = dict()
    # val = set()
    founds = [0 for _ in range(len(val))]
    founds = set()
    for i, coord in enumerate(val):
        if coord not in founds:
            cr = crawler(H, W, val, founds)  # changed for part2
            cr.crawl(coord)
            founds = cr.founds
            new_reg = key + str(reg_num)
            reg_dict[new_reg] = set(cr.path)
            reg_num += 1

    return reg_dict


def part1(imap):
    dict_plot = map_to_dict_plot(imap)
    # print(dict_plot)

    H = len(imap)
    W = len(imap[0])
    regions = []
    # now we find regions for sorted coord
    for key, val in dict_plot.items():
        newreg = coord_to_region(key, val, H, W)
        # breakpoint()
        for reg in newreg.values():
            for r in newreg.values():
                if not reg.isdisjoint(r):
                    pass
        regions.append(newreg)

    print("part1-----------")

    areas = dict()
    pers = dict()
    for reg in regions:
        for k, v in reg.items():
            areas[k] = len(v)
            pers[k] = calc_per(k, v, imap, H, W)

    prices = dict()
    tot_price = 0
    for reg_name, area in areas.items():
        price = area * pers[reg_name]
        prices[reg_name] = price
        tot_price += price
    print(f"total price {tot_price}")

    print("part2-----------")

    # now we got the regions , calc the area and per
    areas = dict()
    pers = dict()
    for reg in regions:
        for k, v in reg.items():
            areas[k] = len(v)
            pers[k] = calc_per2(k, v, imap, H, W)

    prices = dict()
    tot_price = 0
    for reg_name, area in areas.items():
        price = area * pers[reg_name]
        prices[reg_name] = price
        tot_price += price

    print(f"areas sum {sum(areas.values())}, w, h {W}, {H}")

    print(f"total price {tot_price}")


def main():
    # with open("./day12_example.txt") as f:
    with open("./day12_input.txt") as f:
        lines = f.readlines()

    imap = []
    for line in lines:
        line = line.rstrip("\n")
        imap.append(line)

    # print(imap)
    part1(imap)


if __name__ == "__main__":
    main()
