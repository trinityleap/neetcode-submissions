class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return 0

        if len(nums) == 1:
            return nums[0]

        curr = nums[0]
        best = nums[0]

        for i in range(1, len(nums)):
            if curr > 0:
                curr += nums[i]
                
            else:
                curr = nums[i]
            
            best = max(best, curr)
        
        return best