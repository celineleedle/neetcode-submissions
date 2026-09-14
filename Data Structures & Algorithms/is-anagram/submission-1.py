class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sArray = [0 for _ in range(26)]
        tArray = [0 for _ in range(26)]

        for letter in s:
            sArray[ord(letter) - ord('a')] += 1
        for letter in t:
            tArray[ord(letter) - ord('a')] += 1
        
        if sArray == tArray:
            return True
        return False
        
