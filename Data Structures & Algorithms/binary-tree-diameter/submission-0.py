# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        """
        dfs

        trivial solution would be to compute the length of path between any two nodes
        adjacency lists
        """
        if not root:
            return 0

        diameter = 0

        def dfs(node):
            nonlocal diameter 
            # if out of bounds
            if not node:
                return 0
            
            # longest path starting at node?
            left = dfs(node.left)
            right = dfs(node.right)

            diameter = max(diameter, left + right)

            return 1 + max(left, right)

        dfs(root)

        return diameter


