# 140. Word Break II
from collections import defaultdict


# word break II use dict as a dp to save possible combination of word for s[i:n]
def wordBreak(s, wordDict):
    """
    :type s: str
    :type wordDict: List[str]
    :rtype: List[str]
    """
    ls = len(s)
    if ls == 0:
        return []
    dp = defaultdict(list)

    def dfs(s, dp, words):
        if not s:
            return ['']
        if s in dp:
            return dp[s]

        comb = []
        for i in range(len(s)):
            if s[0:i + 1] in words:
                after = dfs(s[i + 1:], dp, words)
                for a in after:
                    comb.append(s[0:i+1]+' '+a)
        dp[s] = comb
        return dp[s]

    return dfs(s, dp, wordDict)


# work break II, a way to use dp to record is s[i:n] is breakable
def wordBreak2(s, wordDict):
    """
    :type s: str
    :type wordDict: List[str]
    :rtype: List[str]
    """
    ls = len(s)
    if ls == 0:
        return []
    word_map = defaultdict(list)
    dp = [True for i in range(ls + 1)]
    dp[ls] = True
    ans = []

    def dfs(s, index, cur, ans, wdict, dp):
        if index == len(s):
            ans.append(cur.rstrip())
            return
        for i in range(index, len(s)):
            if s[index:i + 1] in wdict and dp[i + 1]:
                cur += (s[index:i + 1] + ' ')
                oldsize = len(ans)
                dfs(s, i + 1, cur, ans, wdict, dp)
                if oldsize == len(ans):
                    dp[i + 1] = False
                cur = cur[:-(i + 1 - index + 1)]

    return ans

s = "catsanddog"
d = ["cat","cats","and","sand","dog"]
print wordBreak(s, d)