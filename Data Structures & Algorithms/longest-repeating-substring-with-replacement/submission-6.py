class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = r = 0
        charMap = {}

        maxLength = 0
        maxCharCount = 0

        while r < len(s):
            char = s[r]

            if char not in charMap:
                charMap[char] = 1
            else:
                charMap[char] += 1

            if charMap[char] > maxCharCount:
                maxCharCount = charMap[char]

            numReplacements = r + 1 - l - maxCharCount
            while numReplacements > k:
                charMap[s[l]] -= 1
                numReplacements -= 1
                l += 1

            if r + 1 - l > maxLength:
                maxLength = r + 1 - l

            # print(charMap, l, r, maxLength)

            r += 1

        return maxLength


