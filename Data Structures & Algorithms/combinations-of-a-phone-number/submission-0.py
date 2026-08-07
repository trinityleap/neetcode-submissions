class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        # build map
        letters = { 2 : ['a','b', 'c'],
                3 : ['d', 'e', 'f'], 
                4 : ['g', 'h', 'i'],
                5 : ['j', 'k', 'l'],
                6 : ['m', 'n', 'o'],
                7 : ['p', 'q', 'r', 's'],
                8 : ['t', 'u', 'v'],
                9 : ['w', 'x', 'y', 'z']
                }

        result = []
        def backtrack(digit_index, curr):
            # base: condition met - not sure if correct
            if len(curr) == len(digits):
                result.append(''.join(curr)) 
                return

            for letter in letters[int(digits[digit_index])]:            
                curr.append(letter) # choose - append to string
                # for - in range len map each letter the dig could be?
                backtrack(digit_index + 1, curr) # explore - idk this call
                curr.pop() # backtrack

        backtrack(0, [])
        return result
