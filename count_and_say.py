class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """

        def helper(s):
            if len(s) == 0:
                return ''
            count = 1
            result = ''
            for i in range(1, len(s)):
                if s[i - 1] == s[i]:
                    count += 1
                else:
                    result = str(count) + s[i - 1] + result
                    count = 1
            return str(count) + s[len(s) - 1] + result

        if n == 0:
            return ''
        ans = '1'
        for i in range(n - 1):
            ans = helper(ans)
        return ans

solution = Solution()
print solution.countAndSay(5)