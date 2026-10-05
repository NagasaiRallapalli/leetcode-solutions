class Solution:
    def topKFrequent(self, words: list[str], k: int) -> list[str]:
        freq = {}
        for i in words:
            if i not in freq:
                freq[i] = 1
            else:
                freq[i] += 1

        a = list(freq.keys())
        a.sort()

        for i in range(len(a)):
            for j in range(i + 1, len(a)):
                if freq[a[i]] < freq[a[j]]:
                    a[i], a[j] = a[j], a[i]
                elif freq[a[i]] == freq[a[j]] and a[i] > a[j]:
                    a[i], a[j] = a[j], a[i]
                    
        ans = []
        for i in range(k):
            ans.append(a[i])
        return ans