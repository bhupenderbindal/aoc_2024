import sys
from dataclasses import dataclass
from time import sleep

# import time


@dataclass
class Robo:
    p_i: int
    p_j: int
    v_i: int
    v_j: int

    def simulate(self, time, W, H):

        i_s = self.p_i
        j_s = self.p_j
        # print(i_s, j_s)
        # breakpoint()
        for t in range(time):
            i_n = i_s + self.v_i
            j_n = j_s + self.v_j

            if i_n < 0:
                i_n = H + i_n
            if i_n > H - 1:
                i_n = i_n - H

            if j_n < 0:
                j_n = W + j_n
            if j_n > W - 1:
                j_n = j_n - W

            i_s = i_n
            j_s = j_n
        # maintain the state
        self.p_i = i_n
        self.p_j = j_n
        return i_n, j_n


def part2(robos, H, W, time):

    # final_js = []
    # now remove the items from middle
    q1_x = range(0, int(H / 2))
    q1_y = range(0, int(W / 2))

    q2_x = range(0, int(H / 2))
    q2_y = range(int(W / 2) + 1, W)

    q3_x = range(int(H / 2) + 1, H)
    q3_y = range(0, int(W / 2))

    q4_x = range(int(H / 2) + 1, H)
    q4_y = range(int(W / 2) + 1, W)

    counter = 0
    for _ in range(time):
        final_ps = []
        q1, q2, q3, q4 = [], [], [], []
        for robo in robos:
            i_n, j_n = robo.simulate(1, W, H)
            final_ps.append((i_n, j_n))
            # final_js.append(j_n)
            # print(i_n, j_n)
        # print("888888888888888888")
        draw_shape(W, H, final_ps)

        sleep(1)

        # for i,j in final_ps:
        #     if i in q1_x and j in q1_y:
        #         q1.append((i,j))
        #     if i in q2_x and j in q2_y:
        #         q2.append((i,j))
        #     if i in q3_x and j in q3_y:
        #         q3.append((i,j))
        #     if i in q4_x and j in q4_y:
        #         q4.append((i,j))

        # counter +=1
        # print(len(q1) , len(q2) , len(q3) , len(q4))
        # if len(q1) == len(q2) and len(q3) == len(q4):
        #     q1 = sorted(q1)
        #     q2 = sorted(q2)
        #     q1q2sym = False
        #     for i in range(len(q1)):
        #         breakpoint()
        #         if q1[i][1] + q2[i][1] == W-1:
        #             q1q2sym = True
        #         else:
        #             q1q2sym = False
        #             break
        # if q1q2sym == True:
        # res = len(q1) * len(q2) * len(q3) * len(q4)


def draw_shape(W, H, ps):
    shape = [[" " for _ in range(W)] for _ in range(H)]
    # for row in shape:
    #     print(''.join([str(ss) for ss in row]))
    for i, j in ps:
        # if shape[i][j] == "_":
        shape[i][j] = "*"
    for row in shape:
        print("".join([str(ss) for ss in row]))

    # draw chi
    check_symm(W, H, shape)


def check_symm(W, H, shape):
    mw = int(W / 2)
    mh = int(H / 2)
    symm_count = 0

    for row in shape:
        # if row[0: mw] == row[mw+1:]:
        row = "".join([str(ss) for ss in row])
        try:
            if row[0:mw].rindex("*") == row[mw + 1 :].index("*"):
                symm_count += 1
        except:
            pass
            # print(symm_count)
        # breakpoint()

    if symm_count == H:
        print("symmetric shape")
        for row in shape:
            print("".join([str(ss) for ss in row]))
        breakpoint()


def main(filepath):

    with open(filepath) as f:
        lines = f.readlines()

    print(lines)

    robos = []
    for line in lines:
        line = line.rstrip("\n")
        p_j, p_i = line.split(" ")[0][2:].split(",")
        v_j, v_i = line.split(" ")[1][2:].split(",")

        p_i, p_j = int(p_i), int(p_j)
        v_i, v_j = int(v_i), int(v_j)
        print(p_i, p_j, v_i, v_j)

        robos.append(Robo(p_i, p_j, v_i, v_j))

    # part1(robos)

    # part2(robos,7,11,100)
    part2(robos, 103, 101, 10000000000000000000)


if __name__ == "__main__":

    args = sys.argv
    example_filepath = args[1]
    input_filepath = args[2]

    # main(example_filepath)
    main(input_filepath)
