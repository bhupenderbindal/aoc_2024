import sys
from collections import deque


class BFS:
    def __init__(self, graph_adjacencylist, start, end):
        self.graph = graph_adjacencylist
        self.s = start

    def find_short_path(self, end):

        self.nstate, self.nparent = self.bfs(self.graph, self.s)
        # print(f"nodes state \n: {self.nstate}")
        # print(f"nodes parents\n: {self.nparent}")
        self.root_to_node_path = []
        self.root_to_node(start=self.s, end=end, nparent=self.nparent)
        print(
            f"root to node path: {self.root_to_node_path}, length: {len(self.root_to_node_path) - 1}"
        )

        for i in range(len(self.root_to_node_path) - 1):
            a = self.root_to_node_path[i]
            b = self.root_to_node_path[i + 1]
            diffi = abs(a[0] - b[0])
            diffj = abs(a[1] - b[1])
            if diffi + diffj > 1:
                print("NO PATH FROM START TO END")
                return False, None

        return True, self.root_to_node_path

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

    def root_to_node(self, start, end, nparent):

        if start == end or end == -1:
            self.root_to_node_path.append(start)
        else:
            self.root_to_node(start, nparent[end], nparent)
            self.root_to_node_path.append(end)


def edges_to_adjacencylist(n_nodes, nodes, edges):
    adj_list = dict()
    for i in nodes:
        adj_list[i] = []

    for edge in edges:
        a, b = edge[0], edge[1]
        adj_list[a].append(b)
        adj_list[b].append(a)

    # in case of symmetric grid with two short paths from start to end
    # reversing lists will start bfs from the other node
    # for key, val in adj_list.items():
    #     adj_list[key] = sorted(val, reverse= True)

    print(adj_list)
    return adj_list


def part1(grid, H, W):
    # example graph
    nodes = []
    for i in range(H):
        for j in range(W):
            if grid[i][j] != "#":
                nodes.append((i, j))
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

    print(f"edges: {sorted(edges)}, num of edges {len(edges)}")
    g = edges_to_adjacencylist(n_nodes, nodes, edges)
    bfs = BFS(graph_adjacencylist=g, start=(0, 0), end=(H - 1, W - 1))
    path_found_bool = bfs.find_short_path(end=(H - 1, W - 1))


def part2(grid, H, W, remaining_corrupted):
    # example graph
    nodes = []
    for i in range(H):
        for j in range(W):
            if grid[i][j] != "#":
                nodes.append((i, j))
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

    print(f"edges: {sorted(edges)}, num of edges {len(edges)}")
    g = edges_to_adjacencylist(n_nodes, nodes, edges)
    bfs = BFS(graph_adjacencylist=g, start=(0, 0), end=(H - 1, W - 1))
    path_found_bool, short_path = bfs.find_short_path(end=(H - 1, W - 1))

    oldpath = short_path
    for corrnode in remaining_corrupted:
        # removing corr node from adjacency list and then calc new path
        rmove_from_keys = g.pop(corrnode)
        for key in rmove_from_keys:
            g[key].remove(corrnode)

        if corrnode not in oldpath:
            print(f"node {corrnode} is not in old path")
            pass
        else:
            print(f"node {corrnode} is in old path, NEED TO CHECK NEWPATH")

            bfs = BFS(graph_adjacencylist=g, start=(0, 0), end=(H - 1, W - 1))
            found, new_path = bfs.find_short_path((H - 1, W - 1))
            if found:
                print(f"old path: {oldpath}")
                print(f"new path: {new_path}")
                oldpath = new_path
            else:
                print(f"at this corrnode {corrnode} new path cannot be found")
                break


def main(filepath, H, W, nbytes):
    with open(filepath) as f:
        lines = f.readlines()

    grid = []
    corrupted = []
    for line in lines:
        line = line.rstrip("\n").split(",")
        # inverting x, y from problem statement
        corrupted.append((int(line[1]), int(line[0])))
    print(corrupted)

    corrupted2 = corrupted[:nbytes]
    # create a grid
    grid = [list(range(W)) for _ in range(H)]
    for i in range(H):
        for j in range(W):
            if (i, j) not in corrupted2:
                grid[i][j] = "."
            else:
                grid[i][j] = "#"

    print(grid, H, W)
    part1(grid, H, W)
    part2(grid, H, W, corrupted[nbytes:])


if __name__ == "__main__":
    args = sys.argv

    example_path = args[1]
    input_path = args[2]

    # main(example_path, 7, 7, nbytes= 12)
    main(input_path, 71, 71, nbytes=1024)
