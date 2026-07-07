class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        sliding window
        left = start of string
        right = step through each char in s
        if right = duplicate letter, left = right and start on next substr
        track length of longest substr in best
        track longest substr with left_best
        edge cases: length 0 or 1
        """
        left = 0 
        best_len = 0
        # best_left = 0
        cont = set() # contents of str

        if len(s) == 0 or len(s) == 1:
            return len(s)

        for right in range(len(s)):
            # compare with prev char
            while s[right] in cont: # if right is dup
                cont.remove(s[left]) # reset set
                left += 1 # new window start
        
            cont.add(s[right])
            if right - left + 1 > best_len:
                    best_len = right - left + 1
        
        return best_len
                