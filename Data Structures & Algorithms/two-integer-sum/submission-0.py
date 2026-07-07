class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {} # key = number, value = index
        for i, n in enumerate(nums): # for each number in numbers...
            # if the complement of this number is in seen, return
            comp = target - n
            if comp in seen:
                return [seen[comp], i]

            # if we havent seen this number add it to the dictionary
            if n not in seen:
                seen[n] = i
