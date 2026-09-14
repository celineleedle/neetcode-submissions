class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        numMap = {}
        for num in nums:
            if num not in numMap.keys():
                numMap[num] = 1
            else:
                numMap[num] += 1
        
        currentTop = 0
        res = 0
        for key in numMap.keys():
            if numMap[key] > currentTop:
                res = key
                currentTop = numMap[key]
        return res