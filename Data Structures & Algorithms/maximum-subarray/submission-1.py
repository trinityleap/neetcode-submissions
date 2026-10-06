class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """
        greedy signal: 

        at each position, im tracking the current max subsequence
        and the answer at this position is the sum of the curr max subseq
        """
        if not nums:
            return 0

        if len(nums) == 1:
            return nums[0]

        # track max subarray through item i in nums
        sub = [float('-inf')] * len(nums)
        sub[0] = nums[0]

        for i in range(1, len(nums)): 
        # for each n either add to subarray at prev pos, or start new
            sub[i] = max(sub[i-1]+nums[i], nums[i])
        
        return max(sub)