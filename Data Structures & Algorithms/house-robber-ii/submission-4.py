class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0

        if len(nums) == 1:
            return nums[0]

        def helper(nums):
            if not nums:
                return 0

            if len(nums) == 1:
                return nums[0]
            
            dp = [0] * len(nums) # max robbed from houses 0 through i
            dp[0] = nums[0]

            if nums[0] > nums[1]:
                dp[1] = dp[0]
            else:
                dp[1] = nums[1]

            for i in range(2, len(nums)):
                dp[i] = max(nums[i] + dp[i-2], dp[i-1])

            return dp[len(nums) - 1]

        return max(helper(nums[:-1]), helper(nums[1:]))