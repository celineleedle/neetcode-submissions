class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        r = 0
        window = []
        biggestDiff = 0

        while r < len(arr):
            num = arr[r]

            if len(window) < k:
                # window can grow
                if abs(x - num) > biggestDiff:
                    # better candidate
                    biggestDiff = abs(x - num)
                window.append(num)
            else:
                # window at max

                if abs(x - num) <= biggestDiff:
                    # replace the oldest candidate
                    # but only if it's actually worse
                    # this keeps lower nums with same diff
                    if abs(x - window[0]) > abs(x - num):
                        window = window[1:]
                        window.append(num)

            r += 1

        return window




            