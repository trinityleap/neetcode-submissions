class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        initial thought on solving in O(n) time without div is list slicing, 
            but not sure ab the asymptotics of that
        """

        if not nums:
            return None

        output = [1] * len(nums)
        
        # left
        n = 1
        for i in range(len(nums)):
            output[i] = n
            n *= nums[i]

        # right
        t = 1
        for i in range(len(nums)-1, -1, -1):
            output[i] *= t
            t *= nums[i]
        
        return output