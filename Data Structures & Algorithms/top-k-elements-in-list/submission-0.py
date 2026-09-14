class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numMap = {}
        for num in nums:
            if num not in numMap:
                numMap[num] = 1
            else:
                numMap[num] += 1
        # numMap looks like {1: 1, 2: 1, 3: 2}
        # for nums = [1, 3, 2, 3]
        numArray = [None] * (len(nums) + 1)
        for num, count in numMap.items():
            if numArray[count] is None:
                numArray[count] = [num]
            else:
                numArray[count].append(num)
        
        output = []
        for item in reversed(numArray):
            if item is not None:
                for num in item:
                    if len(output) < k:
                        output.append(num)
        return output
        