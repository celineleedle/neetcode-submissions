class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sArray = [0 for _ in range(26)]
        tArray = [0 for _ in range(26)]

        for letter in s:
            sArray[ord(letter) - ord('a')] += 1
        for letter in t:
            tArray[ord(letter) - ord('a')] += 1
        
        sString = ""
        tString = ""
        for index, count in enumerate(sArray):
            if count != 0:
                sString += f"{index}{count}#"
        for index, count in enumerate(tArray):
            if count != 0:
                tString += f"{index}{count}#"
        
        if sString == tString:
            return True
        return False
        
