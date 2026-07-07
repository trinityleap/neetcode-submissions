class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        Counter(nums)
        .most_common(k)
        for _ in range k
        
        """
        # base case
        if not nums or len(nums) == 1:
            return nums

        top_k = Counter(nums).most_common(k)

        return [n[0] for n in top_k]