class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        seen = set()
        pairs = set()
        for i in nums:
            if i - k in seen:
                pairs.add((i - k, i))
            if i + k in seen:
                pairs.add((i, i + k))
            seen.add(i)
        return len(pairs)