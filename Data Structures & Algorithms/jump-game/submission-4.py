class Solution:
    def canJump(self, nums: List[int]) -> bool:
        reached = 0 # reached index
        i = 0 # index nums
        for i in range(len(nums) - 1):
            if i > reached:
                return False
            
            reached = max(reached, i + nums[i])
    
        if reached >= len(nums) - 1:
            return True
        
        return False
        