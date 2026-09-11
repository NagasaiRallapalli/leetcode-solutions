class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        seen = set()
        result = []
        for i in nums:
            if i not in seen:
                seen.add(i)
            else:
                result.append(i)
        return result