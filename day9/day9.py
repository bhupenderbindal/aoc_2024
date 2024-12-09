
def map_inp_seq(inp):

    nseq = [] 
    start = 0
    for i, ele in enumerate(inp):
        if (i+1) % 2 == 0:
            nseq.extend(list('.'*int(ele)))
        else:
            nseq.extend([str(start) for _ in range(int(ele))])
            start += 1
    return nseq


def map_inp_seq2(inp):

    nseq = [] 
    start = 0
    files_dict ={}
    freespace_dict = {}
    for i, ele in enumerate(inp):
        if (i+1) % 2 == 0:
            a = len(nseq)
            b = a+ int(ele) #- 1
            freespace_dict[(a,b)] = int(ele)
            nseq.extend(list('.'*int(ele)))
        else:
            x = len(nseq)
            y = x+int(ele)
            files_dict[start] = (x,y)
            nseq.extend([str(start) for _ in range(int(ele))])
            start += 1
    return nseq, files_dict, freespace_dict


def part1(inp):
    nseq = map_inp_seq(inp)
    found = True
    l = len(nseq)
    end_i = l-1

    while found:
        if nseq[end_i] != '.':
            try:
                left_i = nseq.index('.',0,end_i+1)

                if left_i <= end_i:
                    nseq[left_i] = nseq[end_i]
                    nseq[end_i] = '.'
                    end_i -= 1
                else:
                    break
            except ValueError as e:
                break
        else:
            end_i -= 1


    sum = 0
    for i, ele in enumerate(nseq):
        if ele != '.':
            sum += i * int(ele)
        else:
            break

    return sum



def part2(inp):
    nseq, files_dict, freespace_dict = map_inp_seq2(inp)
    found = True
    l = len(nseq)


    file_ids_dec = sorted(files_dict.keys(), reverse= True)
    for id in file_ids_dec:
        x, y = files_dict[id]
        blocksize = y-x
        for (i,j) in sorted(freespace_dict.keys()):
            if i < x and j < y: # caused delay in second part
                freesize = freespace_dict[(i,j)]
                if freesize >= blocksize:
                    nseq[i:i+blocksize] = [str(id) for _ in range(blocksize)]
                    nseq[x:y] = ['.' for _ in range(blocksize)]
                    freespace_dict.pop((i,j))
                    # if freespace remains add it to dict
                    if freesize > blocksize:
                        freespace_dict[(i+blocksize, j)] = freesize-blocksize

                    break
        files_dict.pop(id)

    sum = 0
    for i, ele in enumerate(nseq):
        if ele != '.':
            sum += i * int(ele)
        else:
            pass

    return sum


def main():
    # with open("./day9_example.txt") as f:
    with open("./day9_input1.txt") as f:
        lines = f.readlines()

    assert len(lines) == 1
    inp = lines[0].rstrip("\n")

    # print(inp, len(inp))
    res1 = part1(inp)
    print(f"res1 {res1}")
    res2 = part2(inp)
    print(f"res2 {res2}")


if __name__ == "__main__":
    main()