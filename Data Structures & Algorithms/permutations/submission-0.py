class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        """
        backtracking

        """
        if not nums:
            return []

        result = []

        def backtrack(used, curr):
            if len(curr) == len(nums):
                result.append(list(curr))
                return

            for i in range(len(nums)):
                if i in used: # if used index already
                    continue
                curr.append(nums[i])
                used.add(i)
                backtrack(used, curr)
                curr.pop()
                used.remove(i)
            # result.append(list(curr))

        backtrack(set(), [])
        return result