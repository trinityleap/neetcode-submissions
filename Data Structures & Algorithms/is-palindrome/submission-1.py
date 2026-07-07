class Solution:
    def isPalindrome(self, s: str) -> bool:
        # clean string
        s = ''.join(char for char in s if char.isalnum())
        s = s.lower()

        # pointers
        left = 0
        right = len(s) - 1

        while left != right and left <= right:
            # if left and right letter are same, move pointers
            if s[left] == s[right]:
                left += 1
                right -= 1
            # if not, not palindrome
            else:
                return False
        
        return True

