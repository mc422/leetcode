class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """

        def dfs(valuelist, index, length):
            if length == k:
                ans.append(valuelist)
                return
            for i in range(index, n + 1):
                dfs(valuelist + [i], i + 1, length + 1)

        ans = []
        dfs([], 1, 0)
        return ans

solution = Solution()
print solution.combine(4,2)