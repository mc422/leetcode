class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """

        len_a = len(word1)
        len_b = len(word2)
        cnt = [len_a + len_b] * 500
        for j in xrange(0, len_b):
            min_value = 65535
            for i in xrange(0, len_a):
                if cnt[i] < min_value:
                    min_index = i
                    min_value = cnt[i]
                if word1[i] == word2[j]:
                    if min_index < i and min_value - 2 < cnt[i]:
                        cnt[i] = min_value - 2
                    if len_a + len_b - 2 < cnt[i]:
                        cnt[i] = len_a + len_b - 2
                print cnt

        return min(cnt)

s = Solution()
print s.minDistance('abced', 'facad')
