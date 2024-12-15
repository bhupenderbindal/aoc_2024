import sys
from dataclasses import dataclass
from copy import deepcopy

from time import sleep

@dataclass
class MapnRobo:
    mmap: list
    robo: tuple
    
    # it will simulate until all instr are used
    def simulate(self, instr):
        self.H = len(self.mmap)
        self.W = len(self.mmap[0])

        self.print_map(self.mmap)
        for ins in instr:
            # print(ins, self.robo)
            self.move(ins)
            # print(self.robo)
            # self.print_map(self.mmap)
            # sleep(0.1)
        self.print_map(self.mmap)
     
    def move(self, ins):
        if ins == '>':

            i, j = self.robo
            def movebox_right(box):
                if self.mmap[i][box[1]+1] == '.':
                    return box[1]+1
                elif self.mmap[i][box[1]+1] == '#':
                    return None
                else:
                    return movebox_right((box[1]+1, box[1]+2))
            
            if self.mmap[i][j+1] == '.':
                self.mmap[i][j+1] = '@'
                self.robo = (i, j+1)
                self.mmap[i][j] = '.'
            elif self.mmap[i][j+1] == '#':
                pass
            else:
                box = (j+1, j+2)
                j_final = movebox_right(box)
                if j_final:
                    self.mmap[i][j+1:j_final+1] = self.mmap[i][j:j_final]
                    self.mmap[i][j] = '.' 
                    self.robo = (i,j+1)           
        
        if ins == '<':
            i, j = self.robo

            def movebox_left(box):
                if self.mmap[i][box[0]-1] == '.':
                    return box[0]-1
                elif self.mmap[i][box[0]-1] == '#':
                    return None
                else:
                    return movebox_left((box[0]-2, box[0]-1))
            
            if self.mmap[i][j-1] == '.':
                self.mmap[i][j-1] = '@'
                self.robo = (i, j-1)
                self.mmap[i][j] = '.'
            elif self.mmap[i][j-1] == '#':
                pass
            else:
                box = (j-2,j-1)
                j_final = movebox_left(box)
                if j_final:
                    self.mmap[i][j_final:j] = self.mmap[i][j_final+1:j+1]
                    self.mmap[i][j] = '.'
                    self.robo = (i,j-1)            


        if ins == '^':
            i, j = self.robo
            self.mmapcopy = deepcopy(self.mmap)

            def movebox_up(a,b, row):
                if ''.join(self.mmapcopy[row-1][a:b+1]) == '..':
                    self.mmapcopy[row-1][a:b+1] = ['[', ']']
                    return True
                elif ''.join(self.mmapcopy[row-1][a:b+1]) in ['.#', '#.', '##', '#[', ']#']:
                    return False
                elif ''.join(self.mmapcopy[row-1][a:b+1]) == '[]':
                    self.mmapcopy[row-1][a:b+1] = ['[', ']']
                    return movebox_up(a,b, row-1)
                elif ''.join(self.mmapcopy[row-1][a:b+1]) == '].':
                    self.mmapcopy[row-1][a:b+1] = ['[', ']']
                    self.mmapcopy[row-1][a-1] = '.'
                    
                    return movebox_up(a-1,a, row-1)
                elif ''.join(self.mmapcopy[row-1][a:b+1]) == '.[':
                    self.mmapcopy[row-1][a:b+1] = ['[', ']']
                    self.mmapcopy[row-1][b+1] = '.'
                    return movebox_up(b, b+1, row-1) 
                else:
                    self.mmapcopy[row-1][a:b+1] = ['[', ']']
                    self.mmapcopy[row-1][a-1] = '.'
                    self.mmapcopy[row-1][b+1] = '.'
                    
                    return movebox_up(a-1, a, row-1) and  movebox_up(b, b+1, row-1) 
                   
            if self.mmap[i-1][j] == '.':
                self.mmap[i-1][j] = '@'
                self.robo = (i-1, j)
                self.mmap[i][j] = '.'
            elif self.mmap[i-1][j] == '#':
                pass
            elif self.mmap[i-1][j] == ']':
                res = movebox_up(j-1,j, i)
                if res:
                    self.mmapcopy[i-1][j] ='@'
                    self.mmapcopy[i-1][j-1] ='.'
                    self.mmapcopy[i][j] ='.'
                    
                    self.robo = (i-1,j)
                    self.mmap = deepcopy(self.mmapcopy)
    
            elif self.mmap[i-1][j] == '[':
                res = movebox_up(j,j+1, i)
                if res:
                    self.mmapcopy[i-1][j] ='@'
                    self.mmapcopy[i-1][j+1] ='.'
                    self.mmapcopy[i][j] ='.'
                    
                    self.robo = (i-1,j)
                    self.mmap = deepcopy(self.mmapcopy)
            else:
                print("exiting unkown char") # safe check
                exit(0) 
            

        if ins == 'v':
            i, j = self.robo
            self.mmapcopy = deepcopy(self.mmap)
            # rename to down
            def movebox_up(a,b, row):
                if ''.join(self.mmapcopy[row+1][a:b+1]) == '..':
                    self.mmapcopy[row+1][a:b+1] = ['[', ']']
                    return True
                elif ''.join(self.mmapcopy[row+1][a:b+1]) in ['.#', '#.', '##', '#[', ']#']: # some missed cases that occured only with input not examples
                    return False
                elif ''.join(self.mmapcopy[row+1][a:b+1]) == '[]':
                    self.mmapcopy[row+1][a:b+1] = ['[', ']']
                    return movebox_up(a,b, row+1)
                elif ''.join(self.mmapcopy[row+1][a:b+1]) == '].':
                    self.mmapcopy[row+1][a:b+1] = ['[', ']']
                    self.mmapcopy[row+1][a-1] = '.'
                    
                    return movebox_up(a-1,a, row+1)
                elif ''.join(self.mmapcopy[row+1][a:b+1]) == '.[':
                    self.mmapcopy[row+1][a:b+1] = ['[', ']']
                    self.mmapcopy[row+1][b+1] = '.'
                    return movebox_up(b, b+1, row+1) 
                else:
                    # THIS PRINT DEBUGGING SOLVED THE PROBLEM
                    # print(''.join(self.mmapcopy[row+1][a:b+1]))
                    self.mmapcopy[row+1][a:b+1] = ['[', ']']
                    self.mmapcopy[row+1][a-1] = '.'
                    self.mmapcopy[row+1][b+1] = '.'
                    
                    return movebox_up(a-1, a, row+1) and  movebox_up(b, b+1, row+1) 


            if self.mmap[i+1][j] == '.':
                self.mmap[i+1][j] = '@'
                self.robo = (i+1, j)
                self.mmap[i][j] = '.'
            elif self.mmap[i+1][j] == '#':
                pass
            elif self.mmap[i+1][j] == ']':
                res = movebox_up(j-1,j, i)
                if res:
                    self.mmapcopy[i+1][j] ='@'
                    self.mmapcopy[i+1][j-1] ='.'
                    self.mmapcopy[i][j] ='.'
                    
                    self.robo = (i+1,j)
                    self.mmap = deepcopy(self.mmapcopy)
                
            elif self.mmap[i+1][j] == '[':
                res = movebox_up(j,j+1, i)
                if res:
                    self.mmapcopy[i+1][j] ='@'
                    self.mmapcopy[i+1][j+1] ='.'
                    self.mmapcopy[i][j] ='.'
                    
                    self.robo = (i+1,j)
                    self.mmap = deepcopy(self.mmapcopy)
            else:
                print("exiting unkown char") # safe check    
                exit(0)
            
    def print_map(self, mmap):
        for row in mmap:
            print(''.join(row))

def part2(mmap, instr):

    for i, row in enumerate(mmap):
        for j,ch in enumerate(row):
            if ch == '#':
                row[j] = '##'
            if ch == '.':
                row[j] = '..'
            if ch == 'O':
                row[j] = '[]'
            if ch == '@':
                row[j] = '@.'
        temp = []
        for ss in mmap[i]:
            if len(ss) == 2:
                temp.append(ss[0])
                temp.append(ss[1])
            else:
                temp.append(ss)
        mmap[i] = temp
        
    for i, row in enumerate(mmap):
        for j,ch in enumerate(row):
            try:
                j = row.index('@')
                robo = (i,j)
                break
            except:
                pass
    print(robo)
    mapnrobo = MapnRobo(mmap=mmap, robo=robo)
    mapnrobo.simulate(instr=instr)
    
    sum = 0
    for i, row in enumerate(mapnrobo.mmap):
        for j, ch in enumerate(row):
            if ch == '[':
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
    print(mmap, instr)
    part2(mmap, instr)

if __name__ == "__main__":
    args = sys.argv

    example_filepath = args[1]
    input_filepath = args[2]
    
    main(example_filepath)
    main(input_filepath)
