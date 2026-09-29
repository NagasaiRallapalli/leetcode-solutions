class Solution:
    def maxProduct(self, words: list[str]) -> int:
        prod = 0
        seen = []
        for word in words:
            seen.append(set(word))
        for i in range(len(words)):
            for j in range(i + 1, len(words)):
                if not seen[i].intersection(seen[j]):
                    prod = max(prod, len(words[i]) * len(words[j]))
        return prod