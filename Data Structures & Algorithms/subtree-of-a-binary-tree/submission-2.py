# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        """
        subtree must include all sub root's descendants
        """
         
        def isSameTree(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
            if not p: # if no p node
                if q: # if no p node but yes q node
                    return False
                return True # if both nodes are none return true (end of tree)
            elif not q: # if no q node
                if p: # if no q node but yes p node
                    return False
            
            elif p.val != q.val:
                return False
        
            return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)

        # base cases
        if not root:
            if subRoot:
                return False
            return True
        elif not subRoot:
            if root:
                return False


        # if root.val == subRoot.val:
        #     return isSameTree(root, subRoot)
         
        return isSameTree(root, subRoot) or self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        
