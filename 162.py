
def findPeakElement(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    if not nums:
        return 0
    n = len(nums)
    if n == 0:
        return 0
    start, end = 0, n-1
    while start < end:
        mid = start + (end - start)/2
        if nums[mid] < nums[mid+1]:
            start = mid + 1
        elif nums[mid] > nums[mid+1]:
            end = mid
        else:
            end -= 1
    return start

print findPeakElement([1,2,3,1])
