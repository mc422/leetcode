# 287. Find the Duplicate Number

def findDuplicate(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    i = 0
    while i < len(nums):
        if nums[i] == i + 1:
            i += 1
        else:
            if nums[nums[i] - 1] == nums[i]:
                return nums[i]
            else:
                tmp = nums[i]
                nums[i] = nums[nums[i] - 1]
                nums[nums[i] - 1] = tmp
    return 0

print findDuplicate([2,1,1])