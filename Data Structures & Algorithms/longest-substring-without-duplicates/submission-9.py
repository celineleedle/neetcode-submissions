class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        r = 0
        maxLength = 0

        charMap = {}

        for char in s:
            if char not in charMap or charMap[char] == 0:
                charMap[char] = 1
                r += 1

            else:
                while charMap[char] != 0:
                    charMap[s[l]] -= 1
                    l += 1
                charMap[char] = 1
                r += 1

            if r - l > maxLength:
                maxLength = r - l

        return maxLength