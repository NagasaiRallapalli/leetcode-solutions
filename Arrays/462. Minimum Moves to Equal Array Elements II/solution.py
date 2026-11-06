class Solution:
    def minMoves2(self, nums: list[int]) -> int:
        n = len(nums)
        nums.sort()
        if n % 2 == 0:
            median = (nums[n // 2] + (nums[n // 2 - 1])) // 2
        else:
            median = nums[n // 2]
        count = 0
        for i in nums:
            count += abs(i - median)
        return count