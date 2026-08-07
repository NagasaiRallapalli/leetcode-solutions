class Solution(object):
    def removeDuplicates(self, arr):
        if len(arr) == 0:
            return 0
        else:
            j = 0
            for i in range(1, len(arr)):
                if arr[i] != arr[j]:
                    j += 1
                    arr[j] = arr[i]
            return j + 1