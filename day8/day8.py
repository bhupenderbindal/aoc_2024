
def imap_to_antenna_dict(imap, H, W):

    antenna_dict = {}

    for i in range(H):
        w = len(imap[i])
        for j in range(w):
            if imap[i][j] != '.':
                if imap[i][j] not in antenna_dict.keys():
                    antenna_dict[imap[i][j]] = [(i,j)]
                else:
                    antenna_dict[imap[i][j]].append((i,j))

    return antenna_dict

def part1(imap, H, W, antenna_dict):

    antinodes = set()
    for antenna, locations in antenna_dict.items():
        
        for i in range(len(locations)):
            # get_antinode()
            x = locations[i][0]
            y = locations[i][1]
            diffs = [(x-j[0], y-j[1]) for j in locations]
            diffs.remove((0,0))

            # check if twice of diff location is inside imap
            for diff in diffs:
                x_an = x - 2*diff[0]
                y_an = y - 2*diff[1]
                if x_an>=0 and x_an<H and y_an>=0 and y_an<W:
                    # print(f"{imap[x_an][y_an]} at {x_an}, {y_an} is an antinode inside the map for antenna {antenna}")
                    antinodes.add((x_an, y_an))

            pass
    # print(antinodes, len(antinodes))
    return len(antinodes)

def part2(imap, H, W, antenna_dict):

    antinodes = set()
    for antenna, locations in antenna_dict.items():
        
        for i in range(len(locations)):
            # get_antinode()
            x = locations[i][0]
            y = locations[i][1]
            diffs = [(x-j[0], y-j[1]) for j in locations]
            diffs.remove((0,0))
            # adding antinode for each pair with current node at x,y
            for j in locations:
                if x != j[0] and y != j[1]:
                    antinodes.add((j[0], j[1]))

            # check if any multiple of diff location is inside imap
            for diff in diffs:
                multiple = 2
                inside_map= True
                while inside_map:
                    x_an = x - multiple*diff[0]
                    y_an = y - multiple*diff[1]
                    if x_an>=0 and x_an<H and y_an>=0 and y_an<W:
                        # print(f"{imap[x_an][y_an]} at {x_an}, {y_an} is an antinode inside the map for antenna {antenna}")
                        antinodes.add((x_an, y_an))
                        inside_map = True
                    else:
                        inside_map = False
                    multiple += 1

            pass
    # print(antinodes, len(antinodes))
    return len(antinodes)

def main():
    # with open("./day8_example.txt") as f:
    with open("./day8_input.txt") as f:
        lines = f.readlines()
    
    imap = []
    W = 0
    for line in lines:
        line = line.rstrip("\n")
        if len(line)> 0:
            W = len(line)
        imap.append(line)

    H = len(imap)

    antenna_dict = imap_to_antenna_dict(imap, H, W)

    res1 = part1(imap, H, W, antenna_dict)
    print(f"res1 {res1}")
    res2 = part2(imap, H, W, antenna_dict)
    print(f"res2 {res2}")
    
if __name__ == "__main__":
    main()
