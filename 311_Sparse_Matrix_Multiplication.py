def matrix_multiple(m1, m2):
    values1 = {}
    values2 = {}
    
    if len(m1) == 0 or len(m2) == 0:
        return []

    m = len(m1)
    n = len(m1[0])
    w = len(m2[0])

    for i in range(m):
        for j in range(n):
            if m1[i][j] != 0:
                values1[(i, j)] = m1[i][j]

    for i in range(n):
        for j in range(w):
            if m2[i][j] != 0:
                values2[(i, j)] = m2[i][j]

    result = [[0] * w for i in range(m)]
    for i, j in values1.keys():
        for a, b in values2.keys():
            if j == a:
                result[i][b] += values1[(i, j)] * values2[(a, b)]

    return result

A = [
  [ 1, 0, 0],
  [-1, 0, 3]
]

B = [
  [ 7, 0, 0 ],
  [ 0, 0, 0 ],
  [ 0, 0, 1 ]
]

print matrix_multiple(A, B)

