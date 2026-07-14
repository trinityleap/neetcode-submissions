class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        initial thought on solving in O(n) time without div is list slicing, 
            but not sure ab the asymptotics of that
        """

        if not nums:
            return None

        output = [] * len(nums)

        for i in range(len(nums)):
            if nums[i] == 0:
                output.append(math.prod(nums[0:i]+nums[i+1:len(nums)]))

            else:
                output.append(math.prod(nums) // nums[i])
        
        return output