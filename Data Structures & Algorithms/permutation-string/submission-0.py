class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1Map = defaultdict(int)

        for char in s1:
            s1Map[char] += 1

        l = r = 0
        s2Map = defaultdict(int)
        while r < len(s2):
            char = s2[r]
            print(char)
            if char not in s1Map:
                # char not in s1 - not a permutation - move on
                r += 1
                l = r
                s2Map = defaultdict(int) # reset
            else:
                # might be a permutation
                s2Map[char] += 1

                # permutation confirmed
                if s1Map == s2Map:
                    return True

                # otherwise...
                while s2Map[char] > s1Map[char]:
                    # too many of one character
                    # could be new permutation starting from
                    # where the next char after the first in the current window is
                    # so increment l and adjust map accordingly until it's fine
                    leftChar = s2[l]
                    s2Map[leftChar] -= 1
                    l += 1

                r += 1
            print(s1Map, s2Map)

        return False
        

