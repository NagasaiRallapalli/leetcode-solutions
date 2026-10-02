class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        a = []
        for i in range(len(nums) - 1):
            a.append(nums[i + 1] - nums[i])
        if len(nums) <= 1:
            return len(nums)
        low = 0
        high = 1
        count = 1
        while high < len(a) and low < len(a):
            if a[low] == 0:
                low += 1
                continue
            if (a[low] > 0 and a[high] < 0) or (a[low] < 0 and a[high] > 0):
                count += 1
                low = high
            high += 1
        if low < len(a) and a[low] != 0:
            count += 1
        return count