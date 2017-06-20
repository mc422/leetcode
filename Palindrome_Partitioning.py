class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """

        def dfs(valuelist, index):
            if index == len(s):
                ans.append(valuelist)
                return
            for i in range(index, len(s)):
                if dp[index][i]:
                    dfs(valuelist + [s[index:i+1]], i + 1)

        dp = [[False for i in range(len(s))] for j in range(len(s))]
        for i in range(len(s)):
            for j in range(i + 1):
                if i == j:
                    dp[j][i] = True
                elif i - j == 1:
                    dp[j][i] = s[i] == s[j]
                else:
                    dp[j][i] = dp[j + 1][i - 1] and s[j] == s[i]

        ans = []
        dfs([], 0)
        return ans


solution = Solution()
print solution.partition('aab')