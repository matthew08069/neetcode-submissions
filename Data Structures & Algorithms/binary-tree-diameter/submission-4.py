# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # Global var to keep max diameter
        self.res = 0

        # Returns the height
        def dfs(curr):
            # Base case
            if not curr:
                return 0

            left = dfs(curr.left)
            right = dfs(curr.right)

            self.res = max(self.res, left + right)
            return max(left, right) + 1
        # Initiate the recurrsion
        dfs(root)
        return self.res