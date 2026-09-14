class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""
        
        prefix = ""
        j = 0
        for i in range(len(strs[0])):
            for k in range(1, len(strs)):
                if i >= len(strs[k]):
                    return prefix

                if strs[k][j] != strs[0][j]:
                    return prefix
            prefix += strs[0][j]
            j += 1

        return prefix        
