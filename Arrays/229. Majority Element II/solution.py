class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        freq = {}
        for i in nums:
            if i not in freq:
                freq[i] = 1
            else:
                freq[i] += 1
        ans = []
        for key, val in freq.items():
            if val > len(nums) // 3:
                ans.append(key)
        return ans