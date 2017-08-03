# 525. Contiguous Array
# use a count to check the current sum of numbers, if meet 1, add 1, if meet 0, add -1
# and it's index in a dict: map[sum] = index
# if you meet a sum before, that means between the current index and the saved sum index
# the numbers of 0 and 1 are even
import collections


def findMaxLength(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    cnt = collections.defaultdict(int)
    cnt[0] = -1
    sum = 0
    res = 0
    for i, v in enumerate(nums):
        sum += 1 if v == 1 else -1
        if sum not in cnt:
            cnt[sum] = i
        else:

            diff = i - cnt[sum]
            res = max(res, diff)
    return res