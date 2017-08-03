# 399. Evaluate Division

from collections import defaultdict, deque


class Solution(object):
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        divide_map = defaultdict(set)
        value_map = {}
        for i, e in enumerate(equations):
            divide_map[e[0]].add(e[1])
            divide_map[e[1]].add(e[0])
            value_map[tuple([e[0], e[1]])] = values[i]
            value_map[tuple([e[1], e[0]])] = 1 / values[i]

        def find_value(a, b, divide_map, value_map):
            if a not in divide_map:
                return -1
            q = deque()
            q.append(a)
            v = deque()
            v.append(1)
            visited = set()
            visited.add(a)
            while q:
                cur = q.popleft()
                val = v.popleft()
                if cur == b:
                    return val
                else:
                    neighbors = divide_map[cur]
                    for n in neighbors:
                        if n not in visited:
                            q.append(n)
                            pair = tuple([cur, n])
                            v.append(val * value_map[pair])
                            visited.add(n)
            return -1

        ans = []
        for q in queries:
            ans.append(find_value(q[0], q[1], divide_map, value_map))
        return ans


s = Solution()
x = [ ["a","b"],["b","c"] ]
y = [2.0,3.0]
z = [ ["a","c"],["b","c"],["a","e"],["a","a"],["x","x"] ]
print s.calcEquation(x, y, z)