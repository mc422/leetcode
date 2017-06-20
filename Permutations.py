class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans = []
        if len(nums) == 0:
            return ans
        for i in nums:
            if not ans:
                ans.append([i])
            else:
                new_ans = []
                for l in ans:
                    for k in range(len(l)+1):
                        new_list = [digit for digit in l]
                        new_list.insert(k, i)
                        new_ans.append(new_list)
                ans = new_ans
        return

    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        if len(nums) == 0: return []
        if len(nums) == 1: return [nums]
        ans = []
        for i in range(len(nums)):
            if i > 0 and nums[i-1] == nums[i]:
                continue
            else:
                follows = self.permuteUnique(nums[:i] + nums[i+1:])
                for j in follows:
                    ans.append([nums[i]] + j)
        return ans

solution = Solution()
# print solution.permute([1,2,3])
print solution.permuteUnique([1,1,2])