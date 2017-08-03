# 200. Number of Islands

class Solution(object):
    def __init__(self):
        self.ans = 0

    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """

        def dfs(grid, i, j):
            x = len(grid)
            y = len(grid[0])
            if i < 0 or i >= x or j < 0 or j >= y:
                return
            if grid[i][j] == '0' or grid[i][j] == 'x':
                return
            else:
                self.ans += 1

                dfs(grid, i - 1, j)
                dfs(grid, i + 1, j)
                dfs(grid, i, j - 1)
                dfs(grid, i, j + 1)

        dfs(grid, 0, 0)
        return self.ans

test = ["11110","11010","11000","00000"]
s = Solution()
print s.numIslands(test)