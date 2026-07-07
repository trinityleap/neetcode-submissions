class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if not nums or len(nums) < 3:
            return []

        if len(nums) == 3:
            if sum(nums) != 0:
                return []

        triplets = []
        nums.sort()

        for i in range(len(nums) - 1):
            # skip duplicate values for i
            if i > 0 and nums[i] == nums[i-1]:
                continue

            j = i + 1
            k = len(nums) - 1
            
            while j < k:
                target = nums[i] * (-1)
                if nums[j] + nums[k] < target:
                    j += 1
                elif nums[j] + nums[k] > target:
                    k -= 1
                elif nums[j] + nums[k] == target:
                    triplets.append([nums[i], nums[j], nums[k]])
                    
                    # skip duplicates for j and k after finding a triplet
                    while j < k and nums[j] == nums[j+1]:
                        j += 1
                    while j < k and nums[k] == nums[k-1]:
                        k -= 1
                    j += 1
                    k -= 1

        return triplets

