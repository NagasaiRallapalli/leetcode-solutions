class Solution:
    def maxPoints(self, points: list[list[int]]) -> int:
        ans = 1
        for i in range(len(points)):
            freq = {}
            for j in range(len(points)):
                if i == j:
                    continue
                x1, y1 = points[i]
                x2, y2 = points[j]
                dx = x2 - x1
                dy = y2 - y1
                g = math.gcd(dx, dy)
                dx //= g
                dy //= g
                slope = (dx, dy)
                if slope not in freq:
                    freq[slope] = 1
                else:
                    freq[slope] += 1
            if freq:
                ans = max(ans, max(freq.values()) + 1)
        return ans