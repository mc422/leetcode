from collections import defaultdict

import sys


class Solution(object):
    def findMinStep(self, board, hand):
        """
        :type board: str
        :type hand: str
        :rtype: int
        """

        def removeConsecutive(s):
            i, j = 0, 0
            while i < len(s):
                if s[i] == s[j]:
                    i += 1
                elif i - j >= 3:
                    return removeConsecutive(s[0:j] + s[i:])
                else:
                    j = i
            if i - j >= 3:
                s = s[0:j]
            return s

        def helper(board, hand, target):
            board = removeConsecutive(board)

            if not board:
                return 0

            i, j = 0, 0
            ans = sys.maxint
            while i < len(board):
                if board[i] == board[j]:
                    i += 1
                else:
                    need = target - (i - j)
                    if hand[board[j]] >= need:
                        hand[board[j]] -= need
                        after = helper(board[0:j] + board[i:], hand, target)
                        ans = min(after + need, ans)
                        hand[board[j]] += need
                    j = i
            if ans == sys.maxint:
                return -1
            else:
                return ans

        myhand = defaultdict(int)
        for b in hand:
            myhand[b] += 1

        return helper(board, myhand, 3)


a = "WRRBBW"
b = "RB"
s = Solution()
s.findMinStep(a, b)
