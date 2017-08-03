# 209. Minimum Size Subarray Sum
import sys


def minSubArrayLen(s, nums):
    """
    :type s: int
    :type nums: List[int]
    :rtype: int
    """

    i, j = 0, 0
    sum = 0
    ans = sys.maxint
    while j < len(nums):
        sum += nums[j]
        while i <= j and sum >= s:
            if sum == s:
                ans = min(ans, j-i+1)
            sum -= nums[i]
            i += 1
        # if sum == s:
        #     ans = min(ans, j - i + 1)
        # elif sum > s:
        #     while i <= j and sum > s:
        #         sum -= nums[i]
        #         if sum == s:
        j += 1
    if ans == sys.maxint:
        return 0
    else:
        return ans

nums = [1,2,3,4,5]
t = 11

print minSubArrayLen(t, nums)
