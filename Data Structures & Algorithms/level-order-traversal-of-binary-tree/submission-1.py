# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
        helper function?
        """
        if not root:
            return []

        result = []
        queue = [root]

        while queue:
            level = []
            q = []
            while queue:
                curr = queue.pop(0)
                level.append(curr.val)
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
                
                
            queue = q
            result.append(level)

        return result

        