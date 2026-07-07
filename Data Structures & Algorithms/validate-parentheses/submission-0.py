class Solution:
    def isValid(self, s: str) -> bool:
        opens = []

        if len(s) % 2 != 0: # if uneven number of elments
            return False

        pairs = {} # dict w/ key = open, value = closed
        pairs['('] = ')'
        pairs['{'] = '}'
        pairs['['] = ']'

        for char in s:
            if char in pairs: # if open bracket 
                opens.append(char)
            elif not opens: # if finds closed before any open (list empty)
                return False
            else: # if closed bracked
                # if doesnt match most recent open bracket, invalid 
                if pairs[opens.pop()] != char: 
                    return False
        
        if opens: # if open left in list after loop
            return False

        return True

        

        



        