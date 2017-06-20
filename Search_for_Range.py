class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        length = len(nums)
        ans = [-1, -1]
        if length==0:
            return ans
        left, right = 0, length-1
        while left<right:
            mid = (left+right)/2
            if nums[mid] >= target:
                right = mid
            else:
                left = mid+1
        if nums[left] == target:
            ans[0] = left
            while left < length and nums[left]==target:
                ans[1] = left
                left += 1
        return ans

solution = Solution()
print solution.searchRange([2,2], 2)