class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """ 
        binary search mechanism: 
            start at midpoint
            is midpoint target?
                if so return index, end
            if target greater than midpoint, 
                recurse on slice of array midpoint to end
            if target less than midpoint
                recurse on slice of array start to midpoint
            repeat until target found
                if not found return -1
        """

        if not nums:
            return -1

        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if target == nums[mid]:
                return mid

            if target > nums[mid]:
                left = mid + 1
            
            elif target < nums[mid]:
                right = mid - 1
            
        return -1
            
