class Solution:
    def search(self, nums: List[int], target: int) -> int:

        # find cut
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
        cut = left  # index of the smallest element

        def binarySearch(arr, target):
            left = 0
            right = len(arr) - 1

            while left <= right:
                mid = (left + right) // 2

                if arr[mid] == target:
                    return mid

                if arr[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1

            return -1
        
        if target >= nums[cut] and target <= nums[-1]:
            result = binarySearch(nums[cut:], target)
            return result + cut if result != -1 else -1
        else:
            return binarySearch(nums[:cut], target)
