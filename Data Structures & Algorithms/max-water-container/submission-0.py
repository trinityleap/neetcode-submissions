class Solution:
    def maxArea(self, heights: List[int]) -> int:
        """
        for any two bars, max water contained between them = height of lower bar * diff in indices
        trivial to check every pair
        two pointers
        used the hints for the moving the pointers logic, will have to review the intuition there
        """

        if not heights or len(heights) == 1:
            return 0

        left = 0
        right = len(heights) - 1

        maximum = 0

        while left < right:
            if min(heights[left], heights[right]) * (right - left) > maximum:
                maximum = min(heights[left], heights[right]) * (right - left)
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
        
        return maximum