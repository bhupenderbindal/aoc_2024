class Trails:

    def __init__(self):
        self.count_set = set()
        self.rating = 0

    def get_trails(self, imap, i, j, H, W):

        # check in up direction
        ii = i - 1
        jj = j

        if 0 > ii or ii > H - 1 or 0 > jj or jj > W - 1 or imap[ii][jj] == ".":
            pass
        else:
            ii_jj = int(imap[ii][jj])
            i_j = int(imap[i][j])
            if ii_jj - i_j == 1:
                if ii_jj == 9:
                    self.count_set.add((ii, jj))
                    self.rating += 1

                else:
                    self.get_trails(imap, ii, jj, H, W)

        # check down
        ii = i + 1
        jj = j

        if 0 > ii or ii > H - 1 or 0 > jj or jj > W - 1 or imap[ii][jj] == ".":
            pass
        else:
            ii_jj = int(imap[ii][jj])
            i_j = int(imap[i][j])
            if ii_jj - i_j == 1:
                if ii_jj == 9:
                    self.count_set.add((ii, jj))
                    self.rating += 1
                else:
                    self.get_trails(imap, ii, jj, H, W)

        # check right
        ii = i
        jj = j + 1

        if 0 > ii or ii > H - 1 or 0 > jj or jj > W - 1 or imap[ii][jj] == ".":
            pass
        else:
            ii_jj = int(imap[ii][jj])
            i_j = int(imap[i][j])
            if ii_jj - i_j == 1:
                if ii_jj == 9:
                    self.count_set.add((ii, jj))
                    self.rating += 1
                else:
                    self.get_trails(imap, ii, jj, H, W)

        # check left
        ii = i
        jj = j - 1

        if 0 > ii or ii > H - 1 or 0 > jj or jj > W - 1 or imap[ii][jj] == ".":
            pass
        else:
            ii_jj = int(imap[ii][jj])
            i_j = int(imap[i][j])
            if ii_jj - i_j == 1:
                if ii_jj == 9:
                    self.count_set.add((ii, jj))
                    self.rating += 1
                else:
                    self.get_trails(imap, ii, jj, H, W)


def part12(imap, H, W):

    sum1 = 0
    sum2 = 0

    for i, row in enumerate(imap):
        for j, val in enumerate(row):
            if val == "0":
                trails = Trails()
                trails.get_trails(imap, i, j, H, W)
                print(i, j, trails.count_set, len(trails.count_set), trails.rating)

                sum1 += len(trails.count_set)
                sum2 += trails.rating

    print(sum1, sum2)


def main():
    with open("./day10_input.txt") as f:
        # with open("./day10_example.txt") as f:
        lines = f.readlines()

    imap = []
    W = 0
    for line in lines:
        line = line.rstrip("\n")
        if len(line) > W - 1:
            W = len(line)
        imap.append(line)

    H = len(imap)

    print(imap, H, W)
    part12(imap, H, W)


if __name__ == "__main__":
    main()
