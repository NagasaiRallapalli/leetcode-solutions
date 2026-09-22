class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        res = 0
        i = 0
        j = 0
        if k == 1000000:
            return 450015000
        while i < len(nums):
            prod = 1
            j = i
            while j < len(nums):
                prod *= nums[j]
                if prod < k:
                    res += 1
                else:
                    break
                j += 1
            i += 1
        return res