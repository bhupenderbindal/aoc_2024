import sys
from collections import deque
from copy import deepcopy


class BFS:
    def __init__(self, graph_adjacencylist, start, end):
        self.graph = graph_adjacencylist
        self.s = start
        self.nstate, self.nparent = self.bfs(self.graph, self.s)

    def find_short_path(self, start, end, nparent):
        self.root_to_node_path = []

        if start == end:
            return True, [start], 0

        self.root_to_node2(start=start, end=end, nparent=nparent)
        for i in range(len(self.root_to_node_path) - 1):
            a = self.root_to_node_path[i]
            b = self.root_to_node_path[i + 1]
            diffi = abs(a[0] - b[0])
            diffj = abs(a[1] - b[1])
            if diffi + diffj > 1:
                print("NO PATH FROM START TO END")
                return False, None, None

        return True, self.root_to_node_path, len(self.root_to_node_path) - 1

    def bfs(self, graph, s):
        # initialise each vertex state and parent
        nstate = dict()
        nparent = dict()

        for node in graph.keys():
            nstate[node] = "undiscovered"
            nparent[node] = -1

        nstate[s] = "discovered"
        queue = deque([s])

        while len(queue) != 0:
            u = queue.popleft()
            # traversing node next to u
            for v in graph[u]:
                # process edge u to v
                if nstate[v] == "undiscovered":
                    nstate[v] = "discovered"
                    nparent[v] = u
                    queue.append(v)
            nstate[u] = "processed"

        return nstate, nparent

    def root_to_node2(self, start, end, nparent):

        self.root_to_node_path.append(end)

        while True:
            prev = nparent[end]
            self.root_to_node_path.append(prev)
            if prev == start:  # prev = -1 mistake delayed solution
                break
            end = prev
        self.root_to_node_path.reverse()


def edges_to_adjacencylist(n_nodes, nodes, edges):
    adj_list = dict()
    for i in nodes:
        adj_list[i] = []

    for edge in edges:
        a, b = edge[0], edge[1]
        adj_list[a].append(b)
        adj_list[b].append(a)

    return adj_list


def part1(grid, H, W):
    # example graph
    nodes = []
    joiners = dict()
    for i in range(H):
        for j in range(W):
            if grid[i][j] != "#":
                nodes.append((i, j))

                if grid[i][j] == "S":
                    start = (i, j)
                if grid[i][j] == "E":
                    end = (i, j)

                # look for #. right
                # look for #. down
                try:
                    if grid[i][j + 1] == "#" and grid[i][j + 2] != "#":
                        joiners[(i, j + 1)] = [(i, j), (i, j + 2)]
                except:
                    pass

                try:
                    if grid[i + 1][j] == "#" and grid[i + 2][j] != "#":
                        joiners[(i + 1, j)] = [(i, j), (i + 2, j)]
                except:
                    pass

    n_nodes = len(nodes)
    edges = set()
    for node in nodes:
        i, j = node
        r = (i, j + 1)
        d = (i + 1, j)
        if r in nodes:
            edges.add((node, r))
        if d in nodes:
            edges.add((node, d))

    g = edges_to_adjacencylist(n_nodes, nodes, edges)
    bfs = BFS(graph_adjacencylist=g, start=start, end=end)
    nparent = bfs.nparent
    path_found_bool, path, pathlen = bfs.find_short_path(
        start=start, end=end, nparent=nparent
    )
    nparent_rev = dict([(b, a) for a, b in nparent.items()])

    t_initial = pathlen
    removed_hashes = []
    new_path_savings = dict()

    for key, val in joiners.items():
        i1 = path.index(val[0])
        i2 = path.index(val[1])

        if i2 > i1:
            bfs.root_to_node_path = []
            path_found_bool, pathafter, plen = bfs.find_short_path(
                start=path[i2], end=end, nparent=nparent
            )
            if path_found_bool:
                t_beforehash = len(path[:i1])
                t_afterhash = plen
                t_total = t_beforehash + t_afterhash + 2  # extra for connecting hash

                t_saving = t_initial - t_total
                if t_saving in new_path_savings.keys():
                    new_path_savings[t_saving].append(key)
                else:
                    new_path_savings[t_saving] = [key]
                    path

        else:
            path_found_bool, pathafter, plen = bfs.find_short_path(
                start=path[i1], end=end, nparent=nparent
            )
            if path_found_bool:
                t_beforehash = len(path[:i2])
                t_afterhash = plen
                t_total = t_beforehash + t_afterhash + 2  # extra for connecting hash

                t_saving = t_initial - t_total
                if t_saving in new_path_savings.keys():
                    new_path_savings[t_saving].append(key)
                else:
                    new_path_savings[t_saving] = [key]

    atleast = 100
    sum = 0

    for k in sorted(new_path_savings.keys()):

        if k >= atleast:
            sum += len(new_path_savings[k])
    print(f"new path savings {atleast} for {sum} #s")


def main(filepath):
    with open(filepath) as f:
        lines = f.readlines()

    grid = []
    for line in lines:
        grid.append(list(line.rstrip("\n")))

    H = len(grid)
    W = len(grid[0])
    print(grid, H, W)
    part1(grid, H, W)


if __name__ == "__main__":
    args = sys.argv

    example_filepath = args[1]
    input_filepath = args[2]

    # main(example_filepath)
    main(input_filepath)
