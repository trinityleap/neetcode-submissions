
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        brute force approach is multiplying all and construct output as 
            output[i] = product / nums[i] # but this is slow

        is list slicing faster?
        - np.prod
            try and see speed -> mine was too slow
        
        there should be a way to not have to recalculate all sums on each side of nums[i]
        - i cant figure out what it is, i dont see how to combine the other results

        not sure what significance is of each product fitting in 32 bit int
        """
        left = [1]
        right = [1]*len(nums)
        output = [0]*len(nums)

        # left
        for i in range(1, len(nums)):
            left.append(left[i-1]*nums[i-1])
        
        for i in range(len(nums)-2, -1, -1):
            right[i] = (right[i+1]*nums[i+1])

        for i in range(len(nums)):
            output[i] = left[i] * right[i]

        return output