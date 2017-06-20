class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        sign = 1
        if x < 0:
            sign = -1
            x = x*(-1)
        reverse = 0
        prev = 0
        while x>0:
            prev = reverse
            d = x %10
            reverse = reverse * 10 + x % 10
            x = x/10
            if reverse < 0 or (reverse - d) / 10 != prev:
                return 0
        return reverse*sign

solution = Solution()
print solution.reverse(1534236469)