class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = r = 0

        minLength = len(nums) + 1
        currentSum = 0

        while r < len(nums):
            num = nums[r]

            currentSum += num
            # >= target - check subarray length
            while currentSum >= target:
                # update minlength if needed
                if r - l + 1 < minLength:
                    minLength = r - l + 1
                # shrink window
                currentSum -= nums[l]
                l += 1
            # move on
            r += 1
                

        return minLength if minLength != len(nums) + 1 else 0