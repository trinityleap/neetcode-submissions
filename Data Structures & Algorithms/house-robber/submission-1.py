class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        DP -> rather than recursive, 
            store computed values so re-computing is not necessary
        dp[i] stores max money you can rob from houses 0 through i
        decision at each house: skip or rob
        """
        if not nums:
            return 0
        
        dp = [0] * len(nums)

        if len(nums) == 1:
            return nums[0]
            
        if len(nums) == 2:
            return max(nums[0], nums[1])
            
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        i = 2
        while i < len(nums):
            dp[i] = max(dp[i-1], nums[i]+dp[i-2])
            i += 1

        return dp[len(nums) - 1]