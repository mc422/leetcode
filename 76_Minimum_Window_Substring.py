# 76. Minimum Window Substring
# Given a string S and a string T, find the minimum window in S which will contain all the characters in T in complexity O(n).
# For example,
# S = "ADOBECODEBANC"
# T = "ABC"
# Minimum window is "BANC".
# need to use a hashmap to record all word count of string T. Then use TWO POINTER to go through string S.
# use the hashmap and one counter to record if we see a windown contains all char in T,
# then use two pointer, i and j, to find the min window by moving count i and see if still match

from collections import defaultdict


class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        len1 = len(s)
        len2 = len(t)
        if len1 < len2:
            return ''
        words = defaultdict(int)
        for w in t:
            words[w] += 1

        i, j = 0, 0
        cnt = len2
        min_len = len1 + 1
        ans = ''
        while j < len1:
            cur = s[j]
            if cur in words:
                words[cur] -= 1
                if words[cur] >= 0:
                    cnt -= 1

            if cnt == 0:
                while i <= j:
                    prev = s[i]
                    if prev in words:
                        words[prev] += 1
                        if words[prev] > 0:
                            cnt += 1
                    if min_len > j - i + 1:
                        min_len = j - i + 1
                        ans = s[i:j + 1]
                    i += 1
                    if cnt > 0:
                        break
            j += 1
        return ans