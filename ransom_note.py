class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        
        ransom = list(ransomNote)
        magazine = list(magazine)
        
        for i in ransom:
            if i in magazine:
                magazine.remove(i)
            else:
                return False

        return True