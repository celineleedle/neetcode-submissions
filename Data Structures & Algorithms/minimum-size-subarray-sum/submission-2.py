class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = r = 0

        minLength = 0
        currentSum = 0

        while r < len(nums):
            num = nums[r]
            if num >= target:
                return 1

            currentSum += num
            # >= target - check subarray length
            while currentSum >= target and l < r:
                # update minlength if needed
                if r - l + 1 < minLength or minLength == 0:
                    minLength = r - l + 1
                # shrink window
                currentSum -= nums[l]
                l += 1
            # move on
            r += 1
                

        return minLength