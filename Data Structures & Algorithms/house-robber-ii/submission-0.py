class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        dp[i] = max money gained through houses 0 to i

        """
        if not nums:
            return 0
            
        if len(nums) == 1:
            return nums[0]
        
        if len(nums) == 2:
            return max(nums[0], nums[1])

        def robRange(houses):
            if len(houses) == 1:
                return houses[0]

            dp = [0] * len(houses)

            dp[0] = houses[0]
            dp[1] = max(houses[0], houses[1])

            for i in range(2, len(houses)):
                dp[i] = max(dp[i-1], dp[i-2]+houses[i])

            return dp[-1]
         
        return max(robRange(nums[:-1]), robRange(nums[1:]))

        
        