class Solution(object):
    def wordSquares(self, words):
        def dfs(word_list):
            if len(word_list) == length:
                res.append(word_list)
                return
            prefix = ''.join(w[len(word_list)] for w in word_list)
            matchs = dict.get(prefix)
            if matchs:
                for w in matchs:
                    dfs(word_list+[w])

        if len(words) == 0:
            return None
        length = len(words[0])
        dict = {}
        for word in words:
            for i in range(len(word)):
                if word[:i+1] not in dict:
                    dict[word[:i+1]] = []
                dict[word[:i+1]].append(word)

        res = []
        for word in words:
            dfs([word])
        return res

solution = Solution()
words = ["abat","baba","atan","atal"]
print solution.wordSquares(words)