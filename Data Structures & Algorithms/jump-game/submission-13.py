class Solution:
    def canJump(self, nums: List[int]) -> bool:
        """

        start from end: 
            can reach from n:
                canJump(n)


        should i track farthest reached instead?
        """
        if len(nums) == 1:
            return True

        if nums[0] == 0:
            return False

        reached = 0

        for i in range(len(nums)-1):
            if i <= reached and nums[i]:
                # if i+nums[i]
                # reached.append(i+nums[i])
                reached = max(reached, i + nums[i])

        return reached >= (len(nums)-1)

        # dp = [False] * len(nums) # can reach i?

        # dp[0] = True

        # if nums[0] != 0:
        #     dp[1] = True

        # for i in range(1, len(nums)):
        #     if nums[i]:
        #         dp[i+n] = True

        # return dp[len(nums) - 1]