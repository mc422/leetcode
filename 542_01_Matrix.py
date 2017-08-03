import sys
from collections import deque


def updateMatrix(matrix):
    """
    :type matrix: List[List[int]]
    :rtype: List[List[int]]
    """
    m = len(matrix)
    if m == 0:
        return []
    n = len(matrix[0])
    if n == 0:
        return []

    dis = [[m * n for i in range(n)] for j in range(m)]
    for i in range(m):
        for j in range(0, n):
            if matrix[i][j] == 0:
                dis[i][j] = 0
            elif j > 0:
                dis[i][j] = min(dis[i][j], dis[i][j - 1] + 1)
        for j in range(n - 1, -1, -1):
            if matrix[i][j] == 0:
                dis[i][j] = 0
            elif j < n - 1:
                dis[i][j] = min(dis[i][j], dis[i][j + 1] + 1)

    for j in range(n):
        for i in range(0, m):
            if matrix[i][j] == 0:
                dis[i][j] = 0
            elif i > 0:
                dis[i][j] = min(dis[i][j], dis[i - 1][j] + 1)
        for i in range(m - 1, -1, -1):
            if matrix[i][j] == 0:
                dis[i][j] = 0
            elif i < m - 1:
                dis[i][j] = min(dis[i][j], dis[i + 1][j] + 1)
    return dis


def updateMatrixdis(matrix):
    """
    :type matrix: List[List[int]]
    :rtype: List[List[int]]
    """
    m = len(matrix)
    if m == 0:
        return []
    n = len(matrix[0])
    if n == 0:
        return []

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    dis = [[m * n for i in range(n)] for j in range(m)]
    q = deque()

    for i in range(m):
        for j in range(n):
            if matrix[i][j] == 0:
                q.append([i, j])
                dis[i][j] = 0

    while q:
        cur = q.popleft()
        for d in directions:
            x = cur[0] + d[0]
            y = cur[1] + d[1]
            if 0 <= x < m and 0 <= y < n and matrix[x][y] == 1:
                if dis[x][y] > dis[cur[0]][cur[1]] + 1:
                    dis[x][y] = dis[cur[0]][cur[1]] + 1
                    q.append([x, y])

    return dis


test = [[0,1,1,1,1],[1,1,1,1,1],[0,0,0,1,0],[1,0,1,1,1],[1,0,0,0,1]]
test2 = [[0,0,0],[0,1,0],[1,1,1]]

print updateMatrix(test2)
print updateMatrixdis(test)