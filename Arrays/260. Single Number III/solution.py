class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        freq = {}
        s_list = []
        for i in nums:
            if i in freq:
                freq[i] += 1
            else:
                freq[i] = 1
        for key, value in freq.items():
            if value == 1:
                s_list.append(key)
        return s_list