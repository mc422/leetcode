class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """

        def helper(sb, string, level):
            if len(string) == 0:
                if level == 4:
                    ans.append(sb[:-1])
                return
            if level == 4: return
            for i in range(3):
                if i < len(string):
                    part = string[:i + 1]
                    if valid(part):
                        helper(sb + part + '.', string[i + 1:], level + 1)

        def valid(num):
            if len(num) > 1 and num[0] == '0':
                return False
            if 0 <= int(num) <= 255:
                return True
            else:
                return False

        ans = []
        sb = ''
        helper(sb, s, 0)
        return ans

solution = Solution()
print solution.restoreIpAddresses("010010")