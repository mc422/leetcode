# to decide if a graph is a valid Tree, we need to valid if every nodes are connected, and there is no
# loop in the graph

def isValidTree(n, edges):
    def dfs(cur, prev, visited):
        if cur in visited:
            return False
        visited.add(cur)
        for i in paths[cur]:
            if i != prev:
                if not dfs(i, cur, visited):
                    return False
        return True

    paths = [[] for i in range(n)]
    visited = set([])
    for edge in edges:
        paths[edge[0]].append(edge[1])
        paths[edge[1]].append(edge[0])

    if not dfs(0, -1, visited):
        return False

    if len(visited) < n:
        return False
    return True


# using UnionFind
def isValidTree2(n, edges):
    def find_root(x, roots):
        while roots[x] != -1:
            x = roots[x]
        return x

    _roots = [-1 for i in range(n)]
    for edge in edges:
        x = find_root(edge[0], _roots)
        y = find_root(edge[1], _roots)
        if x == y:
            return False
        _roots[x] = y



test1 = [[0, 1], [0, 2], [0, 3], [1, 4]]
test2 = [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]

print isValidTree(5, test1)
print isValidTree(5, test2)