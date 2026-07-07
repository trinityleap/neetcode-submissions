# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """
        recursively swap right and left childs
        """
        
        # base case
        if not root:
            return
        
        temp = root.left
        root.left = root.right
        root.right = temp

        # inverted.append(root.left if root.left)
        # inverted.append(root.right if root.right)

        self.invertTree(root.left)
        self.invertTree(root.right)

        return root
