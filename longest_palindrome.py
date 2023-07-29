class Solution:
    def longestPalindrome(self, s: str) -> int:
        
        initial = len(s)
        sorted_string = sorted(s)
        i = 0

        while i < len(sorted_string) - 1:
            if sorted_string[i] == sorted_string[i+1]:
                del sorted_string[i]
                del sorted_string[i]
            else:
                i=i+1

        no_doubles = len(sorted_string)

        if not no_doubles:
            return initial
        else:
            return initial - no_doubles + 1