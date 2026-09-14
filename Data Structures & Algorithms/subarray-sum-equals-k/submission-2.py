class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefixSum = [0] * len(nums)
        currentSum = 0
        for i in range(len(nums)):
            currentSum += nums[i]
            prefixSum[i] = currentSum

        res = 0
        sumMap = {0: 1}

        for j in range(len(prefixSum)):
            if prefixSum[j] not in sumMap.keys():
                sumMap[prefixSum[j]] = 1
            else:
                sumMap[prefixSum[j]] += 1

            diff = prefixSum[j] - k

            if diff in sumMap.keys():
                res += sumMap[diff]
                if diff == prefixSum[j]:
                    res -= 1

        return res
        