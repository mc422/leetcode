from sys import maxint

def findMinHeightTrees(n, edges):
    connections = {}
    for edge in edges:
        if edge[0] not in connections:
            connections[edge[0]] = []
        connections[edge[0]].append(edge[1])
        if edge[1] not in connections:
            connections[edge[1]] = []
        connections[edge[1]].append(edge[0])

    ans = []
    min = maxint
    for i in range(n):
        visited = []
        queue = [i]
        length = 0
        while queue:
            new_queue = []
            length += 1
            for n in queue:
                visited.append(n)
                if n in connections:
                    for c in connections[n]:
                        new_queue.append(c) if c not in visited else False
            queue = new_queue
        if length < min:
            min = length
            ans = [i]
        elif length == min:
            ans.append(i)
    return ans


def solution2(n, edges):
    remains = n
    connections = [set() for i in range(n)]
    for edge in edges:
        connections[edge[0]].add(edge[1])
        connections[edge[1]].add(edge[0])

    while remains > 2:
        leaves = [k for k, v in enumerate(connections) if len(v) == 1]
        remains -= len(leaves)
        for leave in leaves:
            n = connections[leave].pop()
            connections[n].remove(leave)

    return [k for k, v in enumerate(connections) if len(v)!=0]



n = 6
edges = [[0, 3], [1, 3], [2, 3], [4, 3], [5, 4]]
print solution2(n, edges)