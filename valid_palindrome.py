class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = ''.join(ch for ch in s if ch.isalnum())
        r = s[::-1]
        if r == s:
            return True
        else:
            return False