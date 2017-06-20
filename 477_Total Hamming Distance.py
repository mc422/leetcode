def totalHammingDistance(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    ans = 0
    for i in range(9):
        zero = 0
        one = 0
        for index, val in enumerate(nums):
            if val != 0:
                digit = val & 1
                if digit:
                    one += 1
                else:
                    zero += 1
                nums[index] = val >> 1
            else:
                zero += 1
        print zero, 'and', one
        ans += (zero * one)
    return ans

print totalHammingDistance([1337,7331])