class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        if length == 0:
            return 0
        if length == 1:
            return nums[0]
        max = nums[0]
        min = nums[0]
        res = nums[0]

        for i in range(1, length):
            temp = max
            max = max(nums[i], max * nums[i], min * nums[i])
            min = min(nums[i], temp * nums[i], min * nums[i])
            res = max(res, max)
        return res

solution = Solution()
print solution.maxProduct([1,1,2])