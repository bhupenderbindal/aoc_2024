import itertools

def calc(nums, op_seq, n):
    r = nums[0]

    for i in range(1,n,1):
        if op_seq[i-1] == '+':
            r += nums[i]
        if op_seq[i-1] == '*':
            r *= nums[i] 
    return r

def calc2(nums, op_seq, n):
    r = nums[0]

    for i in range(1,n,1):
        if op_seq[i-1] == '+':
            r += nums[i] 
        if op_seq[i-1] == '*':
            r *= nums[i] 
        if op_seq[i-1] == '|':
            r = int(str(r)+ str(nums[i]))
    return r

def part1(exps, max_n):
    n_to_op_dict = all_op_seq(max_n, opstr = '+*')
    sum = 0
    failed_exps = []

    for exp in exps:
        found = False
        testval = exp[0]
        nums = exp[1]
        n = len(nums)
        op_seqs = n_to_op_dict[n]

        for op_seq in op_seqs:
            if testval == calc(nums, op_seq, n):
                sum += testval
                # break on first match with testval
                found = True
                break
        
        if not found:
            failed_exps.append(exp)
    return sum, failed_exps
        

def part2(failed_exps, max_n, sum1):
    n_to_op_dict = all_op_seq(max_n, opstr = '+*|')
    sum = sum1
    
    for exp in failed_exps:
        found = False
        testval = exp[0]
        nums = exp[1]
        n = len(nums)
        op_seqs = n_to_op_dict[n]

        for op_seq in op_seqs:
            if testval == calc2(nums, op_seq, n):
                sum += testval
                # break on first match with testval
                found = True
                break
        
        if not found:
            pass
            # print(f"not possible for {exp}")
    
    return sum

def all_op_seq(max_n, opstr):
    n_to_op_dict = {}
    
    for i in range(1, max_n+1):
        # n_to_op_dict[i] = op_seq(i)
        # n_to_op_dict[i] = op_seq2(i, opstr='+*')
        seq = [i for i in itertools.product(opstr, repeat=i-1)]
        n_to_op_dict[i] = seq

    return n_to_op_dict

def op_seq(n):

    n_perm = pow(2, n-1)
    exp_sq = []
    for i in range(n_perm):
        width_format = '{0:0'+ str(n-1)+ 'b}'  #'{0:02b}'
        s = width_format.format(i)

        s = s.replace('0', '+')
        s = s.replace('1', '*')
        exp_sq.append(s)
    
    return exp_sq

def op_seq2(n, opstr):

    n= n-1

    perm = itertools.permutations(opstr*(n-1), n)
    perm_set = set(perm)
    # this set misses case with all chars same
    exp_sq = []
    for ps in perm_set:
        exp_sq.append(str(''.join(ps)))

    for i in opstr:
        exp_sq.append((i*n))
    
    return exp_sq



def main():

    # with open("./day7_example.txt") as f:
    with open("./day7_input.txt") as f:
        lines = f.readlines()

    exps = []
    max_n = 0

    for line in lines:
        line = line.rstrip("\n")
        testval, restexp = line.split(":")
        testval = int(testval)
        restexp = restexp.lstrip(" ").split(" ")
        exp_items = tuple(int(i) for i in restexp)
        if len(exp_items) > max_n:
            max_n = len(exp_items)
        exps.append(tuple([testval, exp_items]))
        
    
    sum1, failed_exps = part1(exps, max_n)
    print(f"res1 {sum1}")

    res2 = part2(failed_exps, max_n, sum1)
    print(f"res2 {res2}")
    

if __name__ == "__main__":
    main()
    
    # op_seq generation : binary integers vs permutations
    # print(op_seq2(n, opstr='+*'))
    # print(op_seq(n))
    # print(op_seq2(n, opstr='+*').sort() == op_seq(n).sort())
    
