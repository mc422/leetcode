# Given n nodes labeled from 0 to n - 1 and a list of undirected edges (each edge is a pair of nodes),
# write a function to find the number of connected components in an undirected graph.


def findAllGroups(n, edges):
    if len(edges) == 0:
        return []

    neighbors = [set() for i in range(n)]
    for e in edges:
        neighbors[e[0]].add(e[1])
        neighbors[e[1]].add(e[0])

    q = []
    all = set([i for i in range(n)])
    ans = []

    while all:
        group = []
        next = all.pop()
        # group.append(next)
        q.append(next)
        while q:
            cur = q.pop()
            group.append(cur)
            for n in neighbors[cur]:
                if n in all:
                    all.remove(n)
                    q.append(n)
        ans.append(group)

    return ans


edges =  [[0, 1], [1, 2], [2, 3], [3, 4], [5, 7], [9,7]]
n = 10

print findAllGroups(n, edges)