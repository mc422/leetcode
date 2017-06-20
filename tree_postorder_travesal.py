class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result = []
        if not root:
            return result
        prev = root
        stack = []
        stack.append(root)
        while len(stack)>0:
            cur = stack[len(stack)-1]
            if (cur.left is None and cur.right is None) or cur.left == prev or cur.right == prev:
                stack.pop()
                result.append(cur.val)
            else:
                if cur.right:
                    stack.append(cur.right)
                if cur.left:
                    stack.append(cur.left)
            prev = cur
        return result


n1 = TreeNode(1)
n2 = TreeNode(2)
n3 = TreeNode(3)
n1.left = n2
# n1.right = n3
solution = Solution()
print solution.postorderTraversal(n1)