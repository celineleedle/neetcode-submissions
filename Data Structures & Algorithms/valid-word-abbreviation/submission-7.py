class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        n, m = len(word), len(abbr)
        i = j = 0

        while i < n and j < m:
            if abbr[j] == '0':
                return False

            if word[i] == abbr[j]:
                i += 1
                j += 1
            elif abbr[j].isalpha():
                return False
            else:
                skip = ""
                while j < m and abbr[j].isdigit():
                    skip += abbr[j]
                    j += 1
                i += int(skip)
        
        return i == n and j == m
            