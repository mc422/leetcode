# -*- coding: utf-8 -*-

# 567. Permutation in String

# Sliding Window） 时间复杂度O(n)


from collections import defaultdict


def checkInclusion(s1, s2):
    len1 = len(s1)
    len2 = len(s2)
    if len1 == 0:
        return True
    if len2 == 0:
        return False
    if len1 > len2:
        return False
    cnt = defaultdict(int)
    for w in s1:
        cnt[w] += 1

    i, j = 0, 0
    cur = defaultdict(int)
    counter = 0
    for i in range(len2):
        cur[s2[i]] += 1
        if s2[i] in cnt and cur[s2[i]] <= cnt[s2[i]]:
            counter += 1
        if i >= len1:
            cur[s2[j]] -= 1
            if s2[j] in cnt and cur[s2[j]] < cnt[s2[j]]:
                counter -= 1
            j += 1
        if counter == len1:
            return True
    return False




# bad solution, check each substring one by one, O(nk)
def checkInclusion2(s1, s2):
    """
    :type s1: str
    :type s2: str
    :rtype: bool
    """
    len1 = len(s1)
    len2 = len(s2)
    if len1 == 0:
        return True
    if len2 == 0:
        return False
    if len1 > len2:
        return False
    cnt = defaultdict(int)
    for w in s1:
        cnt[w] += 1

    for i in range(0, len2 - len1 + 1):
        j = 0
        check_cnt = defaultdict(int)
        while j < len1:
            if s2[i + j] in cnt and check_cnt[s2[i + j]] < cnt[s2[i + j]]:
                check_cnt[s2[i + j]] += 1
            else:
                break
            j += 1
        if j == len1:
            return True
    return False


a = "ab"
b="eidbaooo"

print checkInclusion(a, b)

