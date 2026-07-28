class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        """
        dynamic sliding window

        want window to have have one distinct letter aside from k other char
        Counter or hashmap
        - length of Counter (num of distinct keys)
        - stop when sum of values outside of 0th > k
        - add until char not = key with top count

        track longest
        when reset .. reset pointers to... first non top letter from first substring? 
        - no bc BAAABABBAAAABA woudlnt make sense to reset to first B

        helper to find different substrings
        """

        if not s:
            return 0

        if k >= len(s) - 1:
            return len(s)
            
        longest = 0
        left = 0

        valid = Counter()
        freq = 0

        for right in range(len(s)):
            valid[s[right]] += 1   
            freq = max(valid[s[right]], freq)
            
            while (right - left + 1) - freq > k:
                valid[s[left]] -= 1
                left += 1      

            # update longest
            longest = max(longest, right - left + 1)            

        return longest

