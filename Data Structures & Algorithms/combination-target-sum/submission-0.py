class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []

        def backtrack(start, curr, remaining):
            # base cases
            # if valid combination found
            if sum(curr) == target:
                result.append(list(curr))
                return 

            # if overshot
            if remaining < 0:
                return
            
            for i in range(start, len(nums)):
                curr.append(nums[i]) # choose
                backtrack(i, curr, remaining - nums[i]) # explore
                curr.pop() # backtrack

        backtrack(0, [], target)
        return result