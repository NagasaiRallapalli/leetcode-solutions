class Solution(object):
    def thirdMax(self, nums):
        a = sorted(set(nums))
        
        if len(a) < 3:
            return a[-1]
        
        return a[-3]