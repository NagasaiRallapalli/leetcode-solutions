class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        a = set(nums)
        freq = {}
        for i in nums:
            if i not in freq:
                freq[i] = 1
            else:
                freq[i] += 1

        ans = []
        for key, val in freq.items():
            if val == 2:
                ans.append(key)
        for i in range(1, len(nums) + 1):
            if i not in freq:
                ans.append(i)
        return ans            
