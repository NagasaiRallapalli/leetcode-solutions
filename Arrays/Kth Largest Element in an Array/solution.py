class Solution(object):
    def findKthLargest(self, nums, k):
        nums.sort()
        a = nums[::-1]
        return a[k-1]