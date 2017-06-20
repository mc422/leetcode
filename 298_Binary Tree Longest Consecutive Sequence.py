
class Solution:
    max = 0

    def dfs(self, root, target, num):
        if root is None:
            return
        if root.val ==  target:
            num += 1
        else:
            num = 1
        max(max, num)
        self.dfs(root.left, root.val+1, num)
        self.dfs(root.right, root.val+1, num)

    def longest(self, root):
        self.dfs(root, root.val, 0)

