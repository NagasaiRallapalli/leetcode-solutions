class Solution(object):
    def maxSubArray(self, arr):
        a=b=arr[0]
        for i in range(1,len(arr)):
            b=max(arr[i],b+arr[i])
            a=max(a,b)
        return a