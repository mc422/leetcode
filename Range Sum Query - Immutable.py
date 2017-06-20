class NumArray(object):
    def __init__(self, nums):
        """
        initialize your data structure here.
        :type nums: List[int]
        """
        self.sums = [0 for i in range(len(nums) + 1)]
        self.sums[0] = 0
        for i in range(1, len(nums)+1):
            self.sums[i] = self.sums[i - 1] + nums[i-1]

    def sumRange(self, i, j):
        """
        sum of elements nums[i..j], inclusive.
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.sums[j + 1] - self.sums[i]


nums = [-2, 0, 3, -5, 2, -1]
numArray = NumArray(nums)
print numArray.sumRange(0, 1)
print numArray.sumRange(2, 5)