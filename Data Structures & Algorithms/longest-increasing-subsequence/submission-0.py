class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        """
        sliding window
        traverse nums with left and right pointer
        store current longest subsequence
        hashmap/dictionary of with keys = num, values = index in nums of current longest subsequence
        if condition broken, if less than start change start to this value
        if less than end change right to this value and explore length of subsequence, update global if longer
        
        """
        
        if not nums:
            return 0
        if len(nums) == 1:
            return 1

        # array of LIS ending at index i
        # each starts at 1 since every value has min subseq 1 in itself
        sub_lens = [1] * len(nums)

        # for each index, check all previous indices 
        # if value less than current index, 
        # sub_lens[i] can be updated to longest j ending subseq + i
        for i in range(len(nums)):
            for j in range(i):
                if nums[j] < nums[i]:
                    sub_lens[i] = max(sub_lens[i], 1+sub_lens[j])

        return max(sub_lens)

        # best_len = 0
        # best = {nums[0]: 0} # dictionary of 

        # for i, n in enumerate(nums):
        #     if n > max(best): # if num greater than highest val in subseq
        #         best[n] = i
        #         best_len += 1
            
        #     else:
        #         best_len = max(best_len, self.lengthOfLIS(nums[:i]))

        # return best_len

        # elif n < min(best): # if less than least, potential start of new sub
            #     best_len = max(best_len, self.lengthOfLIS(nums[n:]))
