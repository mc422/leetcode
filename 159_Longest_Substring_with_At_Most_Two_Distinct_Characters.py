# [LeetCode] Longest Substring with At Most Two Distinct Characters


from collections import defaultdict


def LongestSubstringTwoDistinct(s, k):
    cnt = defaultdict(int)
    ans = 0
    i, j = 0, 0
    while j < len(s):
        cnt[s[j]] += 1
        while len(cnt) > k:
            cnt[s[i]] -= 1
            if cnt[s[i]] == 0:
                del cnt[s[i]]
            i += 1
        ans = max(ans, j-i+1)
        j += 1

    return ans

print LongestSubstringTwoDistinct('axadaabxxxxxxy', 4)
