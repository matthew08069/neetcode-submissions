# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        # DFS return the sum of root + child
        # Try left child first, if not equal tragetsum, then try right child
        # If DFS finished and no return, return False
        if not root:
            return False

        def dfs(node, total):
            if not node.left and not node.right and node.val + total == targetSum:
                return True
            if node.left:
                if dfs(node.left, node.val + total):
                    return True
            if node.right:
                if dfs(node.right, node.val + total):
                    return True

            return False
        
        return dfs(root, 0)