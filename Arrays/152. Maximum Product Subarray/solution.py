class Solution(object):
    def maxProduct(self, arr):
        c = arr[0]
        c1 = arr[0]
        res = arr[0]

        for i in range(1, len(arr)):
            if arr[i] < 0:
                c, c1 = c1, c

            c = max(arr[i], c * arr[i])
            c1 = min(arr[i], c1 * arr[i])

            res = max(res, c)

        return res