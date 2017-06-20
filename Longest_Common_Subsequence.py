# Longest Common Subsequence

def lcs(word1, word2):
    len1 = len(word1)
    len2 = len(word2)
    dp = [[0] * (len2+1) for _ in range(len1+1)]
    for i in range(1, len1+1):
        for j in range(i, len2+1):
            if word1[i-1] == word2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    return dp[len1][len2]


print lcs('abc', 'wabc')