# 124.Binary Tree Maximum Path Sum

# Definition for a binary tree node.
import sys


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def __init__(self):
        self.ans = -sys.maxint

    # wrong solution, figure out why
    def maxPathSum_bad(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        def dfs(node):
            if not node:
                return 0

            left = dfs(node.left)
            right = dfs(node.right)

            if left:
                left_sum = left + node.val if node.val > 0 else left
                self.ans = max(self.ans, left_sum)
            if right:
                right_sum = right + node.val if node.val > 0 else right
                self.ans = max(self.ans, right_sum)
            self.ans = max(self.ans, left + right + node.val, node.val)

            if max(left, right):
                # WRONG: can choose between left, right or not add any
                return max(node.val+left, node.val+right, node.val)
            else:
                return node.val
        dfs(root)
        return self.ans

    # RIGHT solution
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        def dfs(node):
            if not node:
                return 0

            left_sum = 0
            right_sum = 0

            if node.left:
                left = dfs(node.left)
                left_sum = left if left > 0 else 0
            if node.right:
                right = dfs(node.right)
                right_sum = right if right > 0 else 0

            self.ans = max(self.ans, node.val + left_sum + right_sum)
            return max(node.val, node.val + left_sum, node.val + right_sum)

        dfs(root)
        return self.ans


test = TreeNode(2)
test2 = TreeNode(-1)
test.left = test2
s = Solution()
print s.maxPathSum(test)



