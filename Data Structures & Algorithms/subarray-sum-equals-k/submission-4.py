class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0

        numMap = {0: 1}

        currentSum = 0
        for num in nums:
            currentSum += num
            
            if currentSum not in numMap.keys():
                numMap[currentSum] = 1
            else:
                numMap[currentSum] += 1

            diff = currentSum - k
            if diff in numMap.keys():
                res += numMap[diff]
                if k == 0:
                    res -= 1

        return res

            

