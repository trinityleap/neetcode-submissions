class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        """
        backtracking
        """
        if not nums:
            return [nums]

        result = []
        def backtrack(start, curr):
            # start = starting index
            # curr = nums in current result

            # if starting at last elment
            # if start == len(nums) - 1:
            #     curr.append(nums[start])

            # else:
            for i in range(start, len(nums)):
                curr.append(nums[i])
                backtrack(i + 1, curr)
                curr.pop()
            result.append(list(curr))

        # i keep forgetting that i can run a function without having to return it
        backtrack(0, [])

        return result

            