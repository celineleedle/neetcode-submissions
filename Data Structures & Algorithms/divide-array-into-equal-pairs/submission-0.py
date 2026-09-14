class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        numMap = {}
        for n in nums:
            if n not in numMap.keys():
                numMap[n] = 1
            else:
                numMap[n] += 1
        for key in numMap.keys():
            if numMap[key] % 2 != 0:
                return False

        return True