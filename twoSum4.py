# LeetCode 653

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        if not root:
            return False

        s = set()
        return self.helper(root, s, k)

    def helper(self, root, s, k):
        if not root:
            return False
        if k - root.val in s:
            return True
        s.add(root.val)
        return self.helper(root.left, s, k) or self.helper(root.right, s, k)

