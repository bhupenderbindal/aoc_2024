from scipy import linalg
import numpy as np
from dataclasses import dataclass


@dataclass
class Puzzle:
    puz: str

    def puz_to_mat(self):
        ax = int(self.puz[0].split(",")[0].split("+")[1])
        ay = int(self.puz[0].split(",")[1].split("+")[1])

        bx = int(self.puz[1].split(",")[0].split("+")[1])
        by = int(self.puz[1].split(",")[1].split("+")[1])

        X = int(self.puz[2].split(",")[0].split("=")[1])
        Y = int(self.puz[2].split(",")[1].split("=")[1])

        # mat_A @ vec_N = vec_Z
        mat_A = np.array(([ax, bx], [ay, by]))
        vec_Z = np.array([X, Y])

        return mat_A, vec_Z

    def puz_solve(self, mat_A, vec_Z):
        # calc vec_N [n_a, n_b]
        vec_n = linalg.solve(mat_A, vec_Z)

        if vec_n[0].round(2).is_integer() and vec_n[1].round(2).is_integer():
            return True, vec_n
        else:
            return False, False

    def puz_to_mat2(self):
        ax = int(self.puz[0].split(",")[0].split("+")[1])
        ay = int(self.puz[0].split(",")[1].split("+")[1])

        bx = int(self.puz[1].split(",")[0].split("+")[1])
        by = int(self.puz[1].split(",")[1].split("+")[1])

        X = int(self.puz[2].split(",")[0].split("=")[1]) + 10000000000000
        Y = int(self.puz[2].split(",")[1].split("=")[1]) + 10000000000000

        # mat_A @ vec_N = vec_Z
        mat_A = np.array(([ax, bx], [ay, by]))
        vec_Z = np.array([X, Y])

        return mat_A, vec_Z


def test():
    # mat_A @ vec_N = vec_Z
    mat_A = np.array(([94, 22], [34, 67]))
    vec_Z = np.array([8400, 5400])

    # calc vec_N [n_a, n_b]
    vec_n = linalg.solve(mat_A, vec_Z)
    print(vec_n)


def part1(puzzles):

    tot_tokens = 0
    for puz in puzzles:
        puzo = Puzzle(puz=puz)
        mat_A, vec_Z = puzo.puz_to_mat()
        sol = puzo.puz_solve(mat_A, vec_Z)
        if sol[0]:
            vec_n = sol[1]
            if vec_n[0] <= 100 and vec_n[1] <= 100:
                token_cost = vec_n[0] * 3 + vec_n[1] * 1
                tot_tokens += token_cost
            # breakpoint()

    print(tot_tokens)


def part2(puzzles):

    tot_tokens = 0
    for puz in puzzles:
        puzo = Puzzle(puz=puz)
        mat_A, vec_Z = puzo.puz_to_mat2()
        sol = puzo.puz_solve(mat_A, vec_Z)
        if sol[0]:
            vec_n = sol[1]
            # if vec_n[0] <= 100 and vec_n[1] <= 100:
            token_cost = vec_n[0] * 3 + vec_n[1] * 1
            tot_tokens += token_cost
            # breakpoint()

    print(tot_tokens)


def main():
    # with open("./day13_example.txt") as f:
    with open("./day13_input.txt") as f:
        lines = f.readlines()

    puzzles = []
    singlepz = []
    for line in lines:
        if line != "\n":
            singlepz.append(line.rstrip("\n"))
        else:
            puzzles.append(singlepz)
            singlepz = []

    puzzles.append(singlepz)  # adding the last puzzle

    print(puzzles)
    part1(puzzles)
    part2(puzzles)


if __name__ == "__main__":
    main()
