class Solution:
    def canJump(self, nums: List[int]) -> bool:
        """
        track farthest reached instead
        """
        if len(nums) == 1:
            return True

        if nums[0] == 0:
            return False

        reached = 0

        for i in range(len(nums)-1):
            if i <= reached and nums[i]:
                reached = max(reached, i + nums[i])

        return reached >= (len(nums)-1)