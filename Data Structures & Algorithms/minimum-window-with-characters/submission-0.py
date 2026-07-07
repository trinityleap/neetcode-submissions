class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s or Counter(t) > Counter(s):
            return ''

        left = 0
        needs = Counter(t)

        have = 0 # characters fulfilling their frequency requirements
        required = len(needs)
        window = {}

        result = ''
        result_len = float('inf')

        for right in range(len(s)):
            # add char to window
            c = s[right]
            window[c] = window.get(c, 0) + 1

            # check if requirements for this character are fulfilled
                # if we need this char
                # and if the amount of this char are met
            if c in needs and window[c] == needs[c]:
                have += 1

            # shrink window from the left once conditions met
            while have == required:
                # update result for shrunk window
                if right - left + 1 < result_len:
                    result_len = right - left + 1
                    result = s[left:right+1]
                
                # shrink window from left
                window[s[left]] -= 1
                # if breaks validity
                if s[left] in needs and window[s[left]] < needs[s[left]]:
                    have -= 1
                left += 1

        return result