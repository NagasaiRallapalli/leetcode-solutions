class Solution:
    def wiggleSort(self, nums: list[int]) -> None:
        a = sorted(nums)
        n = len(nums)
        low = (n + 1) // 2 - 1
        high = n - 1
        for i in range(n):
            if i % 2 == 0:
                nums[i] = a[low]
                low -= 1
            else:
                nums[i] = a[high]
                high -= 1