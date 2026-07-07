class Solution:
    def findMin(self, nums: List[int]) -> int:
        if not nums:
            return None

        if len(nums) == 1:
            return nums[0]

        i = 0
        while i < len(nums) - 1 and nums[i] < nums[i+1]:
            i += 1

        if i == len(nums) - 1:
            return nums[0]

        return nums[i+1]