class Solution(object):
    def search(self, nums, t):
        for i in range(len(nums)):
            if nums[i] == t:
                return i
        return -1