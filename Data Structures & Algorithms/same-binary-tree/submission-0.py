class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p: # if no p node
            if q: # if no p node but yes q node
                return False
            return True # if both nodes are none return true (end of tree)
        elif not q: # if no q node
            if p: # if no q node but yes p node
                return False
        
        elif p.val != q.val:
            return False
        
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)