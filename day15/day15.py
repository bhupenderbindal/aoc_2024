import sys
from dataclasses import dataclass

@dataclass
class MapnRobo:
    mmap: list
    robo: tuple

    # it will simulate until all instr are used
    def simulate(self, instr):
        self.H = len(self.mmap)
        self.W = len(self.mmap[0])

        for ins in instr:
            self.move(ins)

    def move(self, ins):
        if ins == '>':
            i, j = self.robo

            if self.mmap[i][j+1] == '.':
                self.mmap[i][j+1] = '@'
                self.robo = (i, j+1)
                self.mmap[i][j] = '.'
            elif self.mmap[i][j+1] == '#':
                pass
            else:
                # move till first nonzero
                for loc in range(j+1, self.W, 1):
                    if self.mmap[i][loc] == '#':
                        break # no movement
                    elif self.mmap[i][loc] == '.':
                        self.mmap[i][j+1] = '@'
                        self.robo = (i, j+1)
                        self.mmap[i][j] = '.'

                        for x in range(j+2,loc+1, 1):
                            self.mmap[i][x] = 'O'
                        break    

        if ins == '<':
            i, j = self.robo

            if self.mmap[i][j-1] == '.':
                self.mmap[i][j-1] = '@'
                self.robo = (i, j-1)
                self.mmap[i][j] = '.'
            elif self.mmap[i][j-1] == '#':
                pass
            else:
                # move till first nonzero
                for loc in range(j-1, -1, -1):
                    # print(i, j, ins, loc)
                    if self.mmap[i][loc] == '#':
                        break # no movement
                    elif self.mmap[i][loc] == '.':
                        self.mmap[i][j-1] = '@'
                        self.robo = (i, j-1)
                        self.mmap[i][j] = '.'

                        for x in range(loc, j-1, 1):
                            self.mmap[i][x] = 'O'
                        break    

        if ins == '^':
            i, j = self.robo

            if self.mmap[i-1][j] == '.':
                self.mmap[i-1][j] = '@'
                self.robo = (i-1, j)
                self.mmap[i][j] = '.'
            elif self.mmap[i-1][j] == '#':
                pass
            else:
                # move till first nonzero
                for loc in range(i, -1, -1):
                    if self.mmap[loc][j] == '#':
                        break # no movement
                    elif self.mmap[loc][j] == '.':
                        self.mmap[i-1][j] = '@'
                        self.robo = (i-1, j)
                        self.mmap[i][j] = '.'

                        for row in range(loc,i-1,1):
                            self.mmap[row][j] = 'O'
                        break    

        if ins == 'v':
            i, j = self.robo

            if self.mmap[i+1][j] == '.':
                self.mmap[i+1][j] = '@'
                self.robo = (i+1, j)
                self.mmap[i][j] = '.'
            elif self.mmap[i+1][j] == '#':
                pass
            else:
                # move till first nonzero
                for loc in range(i, self.H, 1):
                    if self.mmap[loc][j] == '#':
                        break # no movement
                    elif self.mmap[loc][j] == '.':
                        self.mmap[i+1][j] = '@'
                        self.robo = (i+1, j)
                        self.mmap[i][j] = '.'

                        for row in range(i+2, loc+1, 1):
                            self.mmap[row][j] = 'O'
                        break    

    def print_map(self):
        for row in self.mmap:
            print(''.join(row))          

def part1(mmap, instr):

    for i, row in enumerate(mmap):
        try:
            j = row.index('@')
            break
        except:
            pass
    
    mapnrobo = MapnRobo(mmap=mmap, robo=(i,j))
    mapnrobo.simulate(instr=instr)
    
    sum = 0
    for i, row in enumerate(mapnrobo.mmap):
        for j, ch in enumerate(row):
            if ch == 'O':
                sum += i*100 + j
    print(sum)



def main(filepath):
    with open(filepath) as f:
        lines = f.readlines()

    mmap = []
    
    for i, line in enumerate(lines):
        if line != "\n":
            mmap.append(list(line.rstrip("\n")))
        else:
            break

    instr = [i.rstrip("\n") for i in lines[i+1:]]

    instr = ''.join(instr)
    # print(mmap, instr)
    part1(mmap, instr)

if __name__ == "__main__":
    args = sys.argv

    example_filepath = args[1]
    input_filepath = args[2]
    
    main(example_filepath)
    main(input_filepath)
