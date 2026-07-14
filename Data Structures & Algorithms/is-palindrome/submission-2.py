class Solution:
    def isPalindrome(self, s: str) -> bool:
        if not s:
            return False

        # clean and lower string
        pal = ''.join(char for char in s if char.isalnum())
        pal = pal.lower()

        # two pointers
        left = 0
        right = len(pal) - 1

        while left < right:
            if pal[left] != pal[right]:
                return False
            left += 1
            right -= 1
            
        return True