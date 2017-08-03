# 30. Substring with Concatenation of All Words

from collections import defaultdict

def findSubstring(s, words):
    """
    :type s: str
    :type words: List[str]
    :rtype: List[int]
    """
    if len(words) == 0:
        return []

    num = len(words)
    each = len(words[0])

    cnt = defaultdict(int)
    for w in words:
        cnt[w] += 1

    ans = []
    word_num = 0

    for i in range(len(s)):
        if i + each * num <= len(s):
            cur = defaultdict(int)
            word_num = 0
            idx = i
            for j in range(num):
                word = s[idx:idx + each]
                cur[word] += 1
                if word not in cnt or cur[word] > cnt[word]:
                    break
                else:
                    word_num += 1
                idx += each
            if word_num == num:
                ans.append(i)

    return ans




