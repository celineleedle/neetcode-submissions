class Solution:
    def trap(self, height: List[int]) -> int:
        max_left = [0] * len(height)
        max_right = [0] * len(height)
        min_l_r = [0] * len(height)

        max_l = 0
        max_r = 0
        for i in range(len(height)):
            j = len(height) - 1 - i

            max_left[i] = max_l
            max_right[j] = max_r

            if height[i] > max_l:
                max_l = height[i]
            if height[j] > max_r:
                max_r = height[j]

        for i in range(len(height)):
            min_l_r[i] = min(max_left[i], max_right[i])

        res = 0
        for i in range(len(height)):
            res += max(min_l_r[i] - height[i], 0)

        return res

        

        

