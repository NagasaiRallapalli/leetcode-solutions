class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        total_length = len(nums)
        missing = (total_length * (total_length + 1)) // 2
        total_sum = sum(nums)
        return abs(total_sum - missing)