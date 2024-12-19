import sys
import operator as op
from dataclasses import dataclass

@dataclass
class Reg:
    A: int
    B: int
    C: int


def literal_operand(x):
    if x in [0,1,2,3,4,5,6,7]:
        return x
    else:
        print(f"unkown operand {x}, exit")
        return None

def combo_operand(x, reg):

    if x in [0,1,2,3]:
        return x
    elif x == 4:
        return reg.A
    elif x == 5:
        return reg.B
    elif x == 6:
        return reg.C
    elif x == 7:
        print(f"reg {reg} resrved operand 7, exit")
        return None
    else:
        print(f"reg {reg}unkown operand {x}, exit")
        return None

def ins0(operand, reg):

    operand= combo_operand(operand,reg)
    if operand is not None:
        r = reg.A/pow(2, operand)
        r = r.__trunc__() # TODO: truncation vs int 
        reg.A = r
        return None
    
def ins1(operand, reg):
    operand = literal_operand(operand)
    if operand is not None:
        reg.B = op.xor(reg.B, operand)
        return None

def ins2(operand, reg):
    operand= combo_operand(operand,reg)
    if operand is not None:
        r = operand % 8
        reg.B = r
        return None

def ins3(operand, reg):

    operand = literal_operand(operand)
    if operand is not None:
        return operand

def ins4(operand, reg):
    reg.B = op.xor(reg.B, reg.C) # earlier was returning reg.C
    return None

def ins5(operand, reg):

    operand= combo_operand(operand,reg)
    if operand is not None:
        r = operand % 8
        return r

def ins6(operand, reg):
    operand= combo_operand(operand,reg)
    if operand is not None:
        r = reg.A/pow(2, operand)
        r = r.__trunc__()    
        reg.B = r
        return None

def ins7(operand, reg):
    operand= combo_operand(operand,reg)
    if operand is not None:
        r = reg.A/pow(2, operand)
        r = r.__trunc__()
        reg.C = r
        return None

@dataclass
class Inseval:
    instrs: list    # could be tuple
    incr: int
    pointer: int
    reg: Reg
    res: str = ''

    def inseval(self):
        while self.pointer >= 0 and self.pointer <= len(self.instrs)-1:
            opr = self.instrs[self.pointer]
    
            if self.pointer+1 <= len(self.instrs)-1:
                operand = self.instrs[self.pointer+1]
            else:
                operand = None
            
            if opr == 0:
                ins0(operand, self.reg)
                self.pointer += self.incr
            elif opr == 1:
                ins1(operand, self.reg)
                self.pointer += self.incr
            elif opr == 2:
                ins2(operand, self.reg)
                self.pointer += self.incr
            elif opr == 3:
                if self.reg.A == 0:
                    self.pointer += self.incr
                else:
                    jumpto = ins3(operand, self.reg)
                    if jumpto is not None:
                        # print(f"from {self.pointer} jump self.pointer to", jumpto, self.reg) # this jumps the
                        # self.incr = 1 # --------solution --------- misunderstood the statement, this was not required simply
                        self.pointer = jumpto
                    else:
                        # print("no jump---------------------")
                        self.pointer += self.incr
            elif opr == 4:
                ins4(operand, self.reg)
                self.pointer += self.incr
            elif opr == 5:
                res5 = ins5(operand, self.reg)

                if res5 is not None:
                    self.pointer += self.incr
                    self.res += str(res5) + ',' 
            elif opr == 6:
                ins6(operand, self.reg)
                self.pointer += self.incr
            elif opr == 7:
                ins7(operand, self.reg)
                self.pointer += self.incr
            else:
                print(f"unkown operator {opr}, exiting")

def part1():

    # example 
    insev = Inseval(instrs=[2,6], incr=2, pointer=0, reg= Reg(A=0, B=0, C=9))
    insev.inseval()
    assert insev.reg.B == 1
    print(insev.res, insev.reg)


    print("-------------")
    # example 
    insev = Inseval(instrs=[5,0,5,1,5,4], incr=2, pointer=0, reg= Reg(A=10, B=0, C=0))
    insev.inseval()
    assert insev.res == '0,1,2,'
    print(insev.res, insev.reg)


    print("-------------")
    # # example 
    insev = Inseval(instrs=[0,1,5,4,3,0], incr=2, pointer=0, reg= Reg(A=2024, B=0, C=0))
    insev.inseval()
    assert insev.res == '4,2,5,6,7,7,7,7,3,1,0,'
    assert insev.reg.A == 0
    print(insev.res, insev.reg)


    print("-------------")
    # example 
    insev = Inseval(instrs=[1,7], incr=2, pointer=0, reg= Reg(A=0, B=29, C=0))
    insev.inseval()
    assert insev.reg.B == 26
    print(insev.res, insev.reg)

    print("-------------")
    # example 
    insev = Inseval(instrs=[4,0], incr=2, pointer=0, reg= Reg(A=0, B=2024, C=43690))
    insev.inseval()
    assert insev.reg.B == 44354
    print(insev.res, insev.reg)


    print("-------------")
    # example 
    insev = Inseval(instrs=[0,1,5,4,3,0], incr=2, pointer=0, reg= Reg(A=729, B=0, C=0))
    insev.inseval()
    assert insev.res == '4,6,3,5,6,3,5,2,1,0,'
    print(insev.res, insev.reg, ''.join(insev.res.split(',')))


    print("------part 1 -------")
    # example 
    insev = Inseval(instrs=[2,4,1,3,7,5,0,3,4,1,1,5,5,5,3,0], incr=2, pointer=0, reg= Reg(A=45483412, B=0, C=0))
    insev.inseval()
    assert insev.instrs == [2,4,1,3,7,5,0,3,4,1,1,5,5,5,3,0]
    print(insev.pointer, len(insev.instrs))
    print(insev.res, insev.reg, ''.join(insev.res.split(',')))


    print("------part 2 example -------")
    # example 
    insev = Inseval(instrs=[0,3,5,4,3,0], incr=2, pointer=0, reg= Reg(A=2024, B=0, C=0))
    insev.inseval()
    print(insev.pointer, len(insev.instrs))
    print(insev.res, insev.reg, ''.join(insev.res.split(',')))

def part2():
    print("------part 2 example -------")
    i = 0
    found = True 
    while found:
        insev = Inseval(instrs=[0,3,5,4,3,0], incr=2, pointer=0, reg= Reg(A=i, B=0, C=0))
        insev.inseval()
        if insev.res == '0,3,5,4,3,0,':
            print(f"part2: {i}")
            break
        else:
            i += 1
        
    print("------part 2 input -------")
    i = 0
    found = True 
    while found:
        insev = Inseval(instrs=[2,4,1,3,7,5,0,3,4,1,1,5,5,5,3,0], incr=2, pointer=0, reg= Reg(A=i, B=0, C=0))
        insev.inseval()
        if insev.res == '2,4,1,3,7,5,0,3,4,1,1,5,5,5,3,0,':
            print(f"part2: {i}")
            break
        else:
            i += 1
        


def main(filepath):
    with open(filepath) as f:
        lines = f.readlines()

    print(lines)
    part1()
    # part2()


if __name__ == "__main__":
    args = sys.argv

    example_filepath = args[1]
    input_filepath = args[2]
    
    # main(example_filepath)
    main(input_filepath)


    # bin(29)
    # '0b11101'
    # >>> format(29, 'b')
    # '11101'
    # format(0b11101, 'd')
    # '29'
    # int(format(0b11010, 'd'))

    # bitwise xor for int numbers
    # op.xor(29,7)