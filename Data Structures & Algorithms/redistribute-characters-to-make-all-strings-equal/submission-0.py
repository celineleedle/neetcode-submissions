class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        charMap = {}

        for word in words:
            for char in word:
                if char not in charMap.keys():
                    charMap[char] = 1
                else:
                    charMap[char] += 1

        numWords = len(words)
        for key in charMap.keys():
            if charMap[key] % numWords != 0:
                return False

        return True