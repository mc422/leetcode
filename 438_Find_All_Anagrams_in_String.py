# 438. Find All Anagrams in a String
# use slide window algorithm to track the current window you are
# here is all the problems fit in the slide window solution
# https://leetcode.com/problems/minimum-window-substring/
# https://leetcode.com/problems/longest-substring-without-repeating-characters/
# https://leetcode.com/problems/substring-with-concatenation-of-all-words/
# https://leetcode.com/problems/longest-substring-with-at-most-two-distinct-characters/
# https://leetcode.com/problems/find-all-anagrams-in-a-string/

from collections import defaultdict


def findAnagrams(s, p):
    """
    :type s: str
    :type p: str
    :rtype: List[int]
    """
    size = len(p)
    if size > len(s):
        return []
    cnt = 0
    match = defaultdict(int)
    for i in p:
        match[i] += 1

    cur = defaultdict(int)
    ans = []
    for idx, val in enumerate(s):
        # if ind < size:
        if idx >= size:
            prev = s[idx - size]
            if prev in cur:
                cur[prev] -= 1
                if cur[prev] < match[prev]:
                    cnt -= 1
        if val in match:
            cur[val] += 1
            if cur[val] <= match[val]:
                cnt += 1
        if cnt == size:
            ans.append(idx - size + 1)

    return ans


a = "cbaebabacd"
b = "abc"
print findAnagrams(a,b)