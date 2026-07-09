# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def validate(node, maximum, minimum):
            if not node:
                return True
            if node.val >= maximum or node.val <= minimum:
                return False
            return validate(node.left, node.val, minimum) and validate(node.right, maximum, node.val)
        return validate(root, float('inf'), float('-inf'))