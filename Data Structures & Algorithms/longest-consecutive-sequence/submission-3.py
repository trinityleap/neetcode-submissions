class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
        nums.sort
        set to remove duplicates
        sliding window? two pointers?

        starting at end of set, if difference between item and previous item is 1,
        build sequence else go to next item and check condition

        hashmap of set nums pointing to longest consecutive sequence?

        *for each number store longest consecutive sequence up to that number, and 
            if the next item is one greater then their longest is + 1 of the previous
        return max of these

        for i, n in enumerate() OR nested for loops

        is this sort of dp?
        """
        # base
        if not nums:
            return 0

        if len(nums) == 1:
            return 1

        # ordered = sorted(nums) # sorted(n) returns modified list, .sort modifies the list
        u = list(sorted(set(nums))) # list so subscriptable

        # each element makes a sequence of one with itself
        seq_lens = [1] * len(u)


        for i in range(1, len(u)):
            if abs(u[i] - u[i-1]) == 1:
                seq_lens[i] = seq_lens[i-1] + 1

        return max(seq_lens)

