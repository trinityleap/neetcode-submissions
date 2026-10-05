class Solution:
    def isValid(self, s: str) -> bool:
        """
        Stack in python is LIFO, so FILO
        going from the start of the string, 
        the first open bracket should be same type as last closed bracket at the end of the string
        -> treat the string s like a stack
        not sure if efficient to pop so much but will try
        -> use dictionary to match 'types'
        -> compare pop at end to returned value from dict using key = char from start of string
        """
    
        if not s or len(s) % 2 != 0:
            return False

        types = {
            "{" : "}",
            "(" : ")",
            "[" : "]"
        }
 
        opens = []

        for c in s:
            if c in types: # if open
                opens.append(c)
            elif not opens: # if closed before any opens
                return False
            else: # if closed
                if types[opens.pop()] != c:
                    return False

        if opens:
            return False 
            
        return True