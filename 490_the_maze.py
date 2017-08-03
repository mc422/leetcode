

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
            return True
        visited.add(start)

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for d in directions:
            moveto = list(start)
            while 0 <= moveto[0]+d[0] < m and 0 <= moveto[1] + d[1] < n and maze[moveto[0]+d[0]][moveto[1]+d[1]] == 0:
                moveto[0] += d[0]
                moveto[1] += d[1]
            # if moveto[0] == start[0] and moveto[1] == start[1]:
            #     continue
            if tuple(moveto) in visited:
                continue
            if solver(maze, tuple(moveto), target, visited):
                return True
        # visited.remove(start)
        return False

    visited = set()
    return solver(maze, start, end, visited)


test = [
[0, 0, 1, 0, 0],
[0, 0, 0, 0, 0],
[0, 0, 0, 1, 0],
[1, 1, 0, 1, 1],
[0, 0, 0, 0, 0],
        ]
start = (0, 4)
end = (2,4)

print maze_solve(test, start, end)
