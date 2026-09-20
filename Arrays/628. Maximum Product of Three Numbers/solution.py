class Solution:
    def maximumProduct(self, arr: List[int]) -> int:
        arr.sort()
        n = len(arr)
        return max(arr[n - 1] * arr[n - 2] * arr[n - 3] , arr[0] * arr[1] * arr[-1])