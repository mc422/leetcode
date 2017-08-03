# find the shortest distance path from start to end
import sys


def maze_solve(maze, start, end):
    m = len(maze)
    if m == 0:
        return False
    n = len(maze[0])
    if n == 0:
        return False
    if start[0] < 0 or start[0] >= m or start[1] < 0 or start[0] >= n:
        return False
    if end[0] < 0 or end[0] >= m or end[1] < 0 or end[0] >= n:
        return False

    def solver(maze, start, target, visited):
        if start[0] == target[0] and start[1] == target[1]:
            return 0
        visited.add(start)

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        ans = m*n
        found = False
        for d in directions:
            moveto = list(start)
            dis = 0
            while 0 <= moveto[0]+d[0] < m and 0 <= moveto[1] + d[1] < n and maze[moveto[0]+d[0]][moveto[1]+d[1]] == 0:
                moveto[0] += d[0]
                moveto[1] += d[1]
                dis += 1
            # if moveto[0] == start[0] and moveto[1] == start[1]:
            #     continue
            if tuple(moveto) in visited:
                continue
            path = solver(maze, tuple(moveto), target, visited)
            if path != -1:
                ans = min(ans, path+dis)
                found = True
        visited.remove(start)
        if found:
            return ans
        else:
            return -1

    visited = set()
    return solver(maze, start, end, visited)


def maze_bfs(maze, start, end):
    m = len(maze)
    n = len(maze[0])
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    q = []
    distances = [[m*n for i in range(n)] for j in range(m)]
    q.append(start)
    distances[start[0]][start[1]] = 0

    while q:
        cur = q.pop()
        for d in directions:
            x, y = cur[0], cur[1]
            dis = 0
            while 0 <= x+d[0] < m and 0 <= y+d[1] < n and maze[x+d[0]][y+d[1]] == 0:
                x += d[0]
                y += d[1]
                dis += 1
            if distances[cur[0]][cur[1]] + dis < distances[x][y]:
                distances[x][y] = distances[cur[0]][cur[1]] + dis
                if x != end[0] or y != end[1]:
                    q.append([x, y])

    return -1 if distances[end[0]][end[1]] == m*n else distances[end[0]][end[1]]





test = [
[0, 0, 1, 0, 0],
[0, 0, 0, 0, 0],
[0, 0, 0, 1, 0],
[1, 1, 0, 1, 1],
[0, 0, 0, 0, 0],
        ]
start = (0, 4)
end = (4, 4)

print maze_solve(test, start, end)
print maze_bfs(test, start, end)

