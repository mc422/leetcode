# 632. Smallest Range

from collections import defaultdict

import sys


def smallestRange(nums):
    """
    :type nums: List[List[int]]
    :rtype: List[int]
    """

    def smaller(a, b):
        if (a[1] - a[0] < b[1] - b[0]) or (a[1] - a[0] == b[1] - b[0] and a[0] < b[0]):
            return True
        else:
            return False

    all_nums = set()
    num_map = defaultdict(set)
    for idx, val in enumerate(nums):
        all_nums = all_nums.union(set(val))
        for num in val:
            num_map[num].add(idx)

    cnt = [0 for i in range(len(nums))]
    total = 0
    j = 0
    ans = [-sys.maxint, sys.maxint]

    all_nums = list(all_nums)
    all_nums.sort()
    for i in range(len(all_nums)):
        lists = num_map.get(all_nums[i])
        for idx in lists:
            if cnt[idx] == 0:
                total += 1
            cnt[idx] += 1
        if total == len(nums):
            while j <= i and total == len(nums):
                valid = [all_nums[j], all_nums[i]]
                if smaller(valid, ans):
                    ans = valid
                j_lists = num_map.get(all_nums[j])
                for j_idx in j_lists:
                    cnt[j_idx] -= 1
                    if cnt[j_idx] == 0:
                        total -= 1
                j += 1
    return ans


test = [[-5,-4,-3,-2,-1],[1,2,3,4,5]]

print smallestRange(test)
