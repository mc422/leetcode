# 3 solutions:
# 1. use a hashtable to store every number in list 1
# 2. sort arrays, and use two pointer
# 3. use binary search
import collections


def intersection(nums1, nums2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: List[int]
    """
    cnt = collections.defaultdict(int)
    for i in nums1:
        cnt[i] += 1
    ans = []
    for j in nums2:
        if j in cnt:
            ans.append(j)
            del cnt[j]

    return ans