class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        can1 = can2 = -1
        count1 = count2 = 0
        output = []

        for num in nums:
            if num == can1:
                count1 += 1
            elif num == can2:
                count2 += 1
            elif count1 == 0:
                can1 = num
                count1 = 1
            elif count2 == 0:
                can2 = num
                count2 = 1
            else:
                count1 -= 1
                count2 -= 1
            
        count1 = count2 = 0
        for num in nums:
            if num == can1:
                count1 += 1
            elif num == can2:
                count2 += 1
        
        if count1 > len(nums) / 3:
            output.append(can1)
        if count2 > len(nums) / 3:
            output.append(can2)

            
        return output