class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        letters = {
            '2':'abc',
            '3':'def',
            '4':'ghi',
            '5':'jkl',
            '6':'mno',
            '7':'pqrs',
            '8':'tuv',
            '9':'wxyz'
        }

        result = []

        """
        i = current number
        curr = current string
        
        stop when length of string is length of digits = each digit is represented by one of its valid letters

        choose, explore unexplore
        for each letter mapped to each number, 
            choose this* letter -> append to curr, 
            explore -> call backtrack on next letter 
            when valid string made, this* letter popped, 
            repeat for each letter in this string

        confused about why i only need one call to backtrack outside of the method-- 
        actually i get it when i trace through it but idk if id be able to get to it on my own on my first work through
        """
        def backtrack(i, curr):
            if i == len(digits):
                result.append(''.join(curr))
                return # forgot this

            # choose, explore, unchoose
            # handle 3 letters per num w loop
            for c in letters[digits[i]]:
                curr.append(c)
                backtrack(i + 1, curr)
                curr.pop()
            
        backtrack(0, [])
        return result
