class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        l, r = 0, k
        # window starts from 0 up to (not including) element at k

        while r < len(arr):
            # need to check if this new element is better than the leftmost of window
            # since that would be what gets dropped
            num = arr[r]
            if abs(num - x) < abs(arr[l] - x):
                # strictly less than - so in case of tie we ignore the bigger element
                # shrink the window to include this new element
                l += 1
            elif abs(num - x) == abs(arr[l] - x) and num == arr[l]:
                # if they're the same number we continue sliding
                l += 1

            # move onto next
            r += 1
            # print(arr[l:l+k])
        return arr[l:l+k]