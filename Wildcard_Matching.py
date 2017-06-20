class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        match = [[False for i in range(len(s) + 1)] for j in range(len(p) + 1)]
        match[0][0] = True

        for i in range(1, len(p) + 1):
            for j in range(len(s) + 1):
                if p[i - 1] == '*':
                    match[i][j] = match[i - 1][j] or match[i][j - 1]
                else:
                    if j==0:
                        match[i][j] = False
                    else:
                        match[i][j] = match[i - 1][j - 1] and (s[j - 1] == p[i - 1] or p[i-1] == '?')
        return match[len(p)][len(s)]

    def isMatch2(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        dp = [False for i in range(len(s)+1)]
        dp[0] = True

        for i in range(len(p)):
            # if p[i] == '*':
            #     for j in range(len(s)+1):
            #         if i == 0:
            #             dp[j] = True;
            #         else:
            #             if j>0:
            #                 dp[j] = dp[j] or dp[j - 1]
            #             else:
            #                 dp[j] = dp[j]
            # else:
            #     for j in reversed(range(len(s)+1)):
            #         if j > 0:
            #             dp[j] = dp[j - 1] and (s[j-1] == p[i] or p[i] == '?')
            if p[i] == '*':
                for j in range(len(s)+1):
                    if j == 0:
                        dp[j] = dp[j]
                    else:
                        dp[j] = dp[j] or dp[j-1]
            else:
                for j in reversed(range(len(s)+1)):
                    if j > 0:
                        dp[j] = dp[j - 1] and (s[j-1] == p[i] or p[i] == '?')
                    else:
                        dp[j] = False

        return dp[len(s)]

solution = Solution()
print solution.isMatch2('aacdd*ddc', '*')