class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = r = 0
        charMap = {}

        maxCharCount = 0
        maxLength = 0
        maxChar = s[0]


        while r < len(s):
            char = s[r]

            if char not in charMap:
                charMap[char] = 1
            else:
                charMap[char] += 1

            if charMap[char] > maxCharCount:
                maxCharCount = charMap[char]
                maxChar = char

            numReplacements = r + 1 - l - maxCharCount
            while numReplacements > k:
                charMap[s[l]] -= 1
                if s[l] == maxChar:
                    maxCharCount -= 1

                numReplacements -= 1
                l += 1

            if r + 1 - l > maxLength:
                maxLength = r + 1 - l

            # print(charMap, l, r, maxLength)

            r += 1

        return maxLength


