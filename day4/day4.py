
def get_lr(rows, W, H):

    list_lr = rows
    return list_lr

def get_ud(rows, W, H):
    list_ud = []
    # for row in 
    for i in range(W):
        list_ud.append([row[i] for row in rows])
    
    return list_ud

def get_r_ud(rows, W, H):

    list_r_ud = []
    for i in range(H):
        ii = i
        jj = 0
        ru = []
        while ii < W and jj < H and ii>=0 and jj>=0:

            ru.append(rows[ii][jj])
            ii -= 1
            jj += 1

        list_r_ud.append(ru)

    for i in range(H):
        ii = i
        jj = 0
        rd = []
        while ii < W and jj < H and ii>=0 and jj>=0:

            rd.append(rows[ii][jj])
            ii += 1
            jj += 1

        list_r_ud.append(rd)
    # print(list_r_ud)
    return list_r_ud

def get_l_ud(rows, W, H):

    list_l_ud = []
    # reject first and last row as already included in get_r_ud
    for i in range(1,H-1,1):
        ii = i
        jj = W-1
        lu = []
        while ii < W and jj < H and ii>=0 and jj>=0:

            lu.append(rows[ii][jj])
            ii -= 1
            jj -= 1

        list_l_ud.append(lu)

    for i in range(1,H-1,1):
        ii = i
        jj = W-1
        ld = []
        while ii < W and jj < H and ii>=0 and jj>=0:

            ld.append(rows[ii][jj])
            ii += 1
            jj -= 1

        list_l_ud.append(ld)

    # print(list_l_ud)
    return list_l_ud


def find_xmas(s):
    count = 0
    original_s = s
    # both forward and backward
    i = 0
    while len(s) > 0:
        try:
            found = s[i:].index("XMAS")
            count += 1
            s = s[found+4:]
        except ValueError:
            s = s[i+1:]

    # now repeat for reversed
    sr = ""
    for i in reversed(original_s):
        sr += i
    
    i = 0
    while len(sr) > 0:
        try:
            found = sr[i:].index("XMAS")
            count += 1
            sr = sr[found+4:]
        except ValueError:
            sr = sr[i+1:]
    
    
    return count





def part1(rows, W, H):

    sum = 0
    list_all = []
    
    list_lr = get_lr(rows, W, H)
    list_all.extend(list_lr)
    # print(list_lr)
    list_ud = get_ud(rows, W, H)
    list_all.extend(list_ud)
    # # print(list_ud)

    list_r_ud = get_r_ud(rows, W, H)
    list_all.extend(list_r_ud)
    
    list_l_ud = get_l_ud(rows, W, H)
    # print(list_l_ud)
    list_all.extend(list_l_ud)
    
    for item in list_all:
        s = "".join(item)
        sum += find_xmas(s)
    print(sum)

    # get_l_ud(rows, W, H)


def part2(rows, W, H):
    sum = 0

    permutations = [['M', 'S', 'S', 'M'], ['M', 'M', 'S', 'S'], ['S', 'S', 'M', 'M'],  ['S', 'M', 'M', 'S']]

    # find all A occurence and their neighbors
    a_pos = []
    for i in range(H):
        row = rows[i]
        for j in range(W):
            if row[j] == 'A':
                a_pos.append((i,j))

    print(a_pos)

    a_cw_list = []

    for i,j in a_pos:
        a_neighbors = []
        
        try: 
            if i-1>=0 and j-1>=0:
                a_neighbors.append(rows[i-1][j-1])
        except: 
            pass
        try: 
            if i-1>=0 :
                a_neighbors.append(rows[i-1][j+1])
        except: 
            pass
        try: 
            a_neighbors.append(rows[i+1][j+1])
        except: 
            pass
        try:
            if j-1>=0:
                a_neighbors.append(rows[i+1][j-1])
        except: 
            pass
        
        if a_neighbors in permutations:
            sum += 1
        a_cw_list.append(a_neighbors)

    print(a_cw_list)
    print(sum)


def main():

    with open("./day4_input.txt", newline= '') as f:
    # with open("./day4_example.txt", newline= '') as f:
        lines = f.readlines()

    rows = []
    for line in lines:
        line = line.rstrip('\n')
        rows.append([i for i in line])
    
    H = len(rows)
    W = len(rows[0])
    print(W, H)
    
    part1(rows, W, H)
    part2(rows, W, H)



if __name__ == "__main__":
    main()

