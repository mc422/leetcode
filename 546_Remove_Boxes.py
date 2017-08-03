

def removebox(s):
    if not s:
        return 0

    i, j = 0, 0
    ans = 0
    while i < len(s)+1:
        if i < len(s) and s[i] == s[j]:
            pass
        else:
            after = removebox(s[:j]+s[i:])
            ans = max(ans, after+(i-j)*(i-j))
            j = i
        i += 1
    return ans


class Solution(object):
    def __init__(self):
        self.map = {}

    def removeBoxes(self, boxes):
        """
        :type boxes: List[int]
        :rtype: int
        """
        s = boxes
        if not s:
            return 0
        if tuple(s) in self.map:
            return self.map.get(tuple(s))

        i, j = 0, 0
        ans = 0
        while i < len(s) + 1:
            if i < len(s) and s[i] == s[j]:
                pass
            else:
                after = self.removeBoxes(s[:j] + s[i:])
                ans = max(ans, after + (i - j) * (i - j))
                j = i
            i += 1
        self.map[tuple(s)] = ans
        return ans


test = [1, 3, 2, 2, 2, 3, 4, 3, 1]

s = Solution()
print removebox(test)
print s.removeBoxes(test)