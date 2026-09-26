class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        n = len(nums)
        count = float('inf')
        total = 0
        i = 0
        for j in range(i, n):
            total += nums[j]
            while total >= target:
                count = min(count, j - i + 1)
                total -= nums[i]
                i += 1
                    
        if count == float('inf'):
            return 0
        return count