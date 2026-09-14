class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        i, j = 0, 0

        while i < len(word) and j < len(abbr):

            skip = ""
            while j < len(abbr) and abbr[j].isdigit():
                skip += abbr[j]
                j += 1
            if skip.startswith("0"):
                return False

            skipped = 0
            while skip and skipped < int(skip):
                i += 1
                skipped += 1
                if i == len(word) and skipped != int(skip):
                    return False

            if i == len(word) and skipped == int(skip) and j == len(abbr):
                return True
            if i >= len(word):
                return False

            if word[i] != abbr[j]:
                return False

            i += 1
            j += 1

        return True