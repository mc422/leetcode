# coding=utf-8


# There is a ball in a maze with empty spaces and walls. The ball can go through empty spaces
#  by rolling up (u), down (d), left (l) or right (r), but it won't stop rolling until hitting
# a wall. When the ball stops, it could choose the next direction. There is also a hole in this maze.
# The ball will drop into the hole if it rolls on to the hole.

# Given the ball position, the hole position and the maze, find out how the ball could drop into
# the hole by moving the shortest distance. The distance is defined by the number of empty spaces
#  traveled by the ball from the start position (excluded) to the hole (included). Output the moving
#  directions by using 'u', 'd', 'l' and 'r'. Since there could be several different shortest ways,
# you should output the lexicographically smallest way. If the ball cannot reach the hole, output "impossible".


# 还需要用一个哈希表来建立每个位置跟滚到该位置的方向字符串之间的映射，这里我们用一个trick，将二维坐标转(i,j)为一个数字i*n+j
def maze_bfs(maze, start, end):
    m = len(maze)
    n = len(maze[0])
    map = {
        (-1, 0): 'up',
        (1, 0): 'down',
        (0, -1): 'left',
        (0, 1): 'right'
    }
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    q = []
    ans = 'impossible'
    path = ''
    distances = [[m * n for i in range(n)] for j in range(m)]
    q.append([start, path])
    distances[start[0]][start[1]] = 0

    while q:
        cur = q.pop()
        for d in directions:
            x, y = cur[0][0], cur[0][1]
            path = cur[1]
            dis = 0
            while 0 <= x + d[0] < m and 0 <= y + d[1] < n and maze[x + d[0]][y + d[1]] == 0:
                x += d[0]
                y += d[1]
                dis += 1
                if x == end[0] and y == end[1]:
                    break

            path = (path + map.get(d) + '->')
            if distances[cur[0][0]][cur[0][1]] + dis < distances[x][y]:
                print cur[0][0], cur[0][1], distances[cur[0][0]][cur[0][1]] + dis
                distances[x][y] = distances[cur[0][0]][cur[0][1]] + dis
                if x == end[0] and y == end[1]:
                    ans = max(ans, path)
                if x != end[0] or y != end[1]:
                    q.append([[x, y], path])

    return ans


test = [
    [1, 0, 0, 0, 0],
    [1, 0, 0, 0, 1],
    [0, 0, 0, 0, 0],
    [0, 1, 0, 0, 1],
    [0, 1, 0, 0, 0],
]

start = (4, 3)
end = (2, 4)

print maze_bfs(test, start, end)
