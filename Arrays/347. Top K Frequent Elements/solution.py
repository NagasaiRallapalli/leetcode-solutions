class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        a = []
        c = list(set(nums))
        b = []

        for i in c:
            b.append(nums.count(i))

        while k > 0:
            m = max(b)
            x = b.index(m)
            a.append(c[x])
            c.pop(x)
            b.pop(x)
            k -= 1

        return a