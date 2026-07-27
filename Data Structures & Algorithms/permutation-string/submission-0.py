class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        """
        sliding window

        bases:
            is s2 at least as long as s1 
                or counter s2 > s1 
                otherwise containing perm is not possible
        
        window size of s1, 
            slide until counter window = counter s1
        - how to track whats in window?
        - computing counter at each update might be inefficient

        """

        # base
        if Counter(s1) > Counter(s2):
            return False
        
        #
        left, right = 0, len(s1) - 1
        while right < len(s2):
            curr = Counter(s2[left:right+1])
            
            if Counter(s1) == curr:
                return True

            left += 1
            right += 1

        return False
