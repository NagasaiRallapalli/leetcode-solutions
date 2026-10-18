class Solution:
    def canReorderDoubled(self, arr: List[int]) -> bool:
        freq = {}
        for i in arr:
            if i not in freq:
                freq[i] = 1
            else:
                freq[i] += 1

        a = list(freq.keys())
        a.sort(key = abs)

        for i in a:
            if freq[i] == 0:
                continue
            if 2 * i not in freq:
                return False
            if freq[2 * i] < freq[i]:
                return False
                
            freq[2 * i] -=  freq[i]
            freq[i] = 0
        return True