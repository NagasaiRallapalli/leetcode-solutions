class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        nums = list(set(nums))
        nums.sort()
        count = 1
        max_sum = 1
        for i in range(len(nums)-1):
            if nums[i+1] - nums[i] == 1:
                count += 1
            else:
                max_sum = max(max_sum, count)
                count = 1
        max_sum = max(max_sum , count)
        return max_sum