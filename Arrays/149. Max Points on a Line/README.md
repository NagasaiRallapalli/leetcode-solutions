# Max Points on a Line

![LeetCode](https://img.shields.io/badge/LeetCode-149-orange)
![Difficulty](https://img.shields.io/badge/Difficulty-Hard-red)

## 📌 Problem

Given an array of points where `points[i] = [xi, yi]` represents a point on the X-Y plane, return the maximum number of points that lie on the same straight line.

### Example

**Input:**

```text
points = [[1,1],[2,2],[3,3]]
```

**Output:**

```text
3
```

**Explanation:**

All three points lie on the same straight line.

## 🚀 Approach

For every point, consider it as the starting point.

* Calculate the difference in `x` and `y` coordinates with every other point.
* Use `math.gcd()` to reduce the slope into a normalized `(dx, dy)` pair.
* Store the normalized slope and its frequency in a dictionary.
* The slope with the highest frequency represents the maximum number of other points on the same line.
* Add `1` for the starting point itself.

To keep the same line represented by the same slope, the sign is normalized when `dx < 0`.

## 💻 Solution

```python
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

                if dx < 0:
                    dx = -dx
                    dy = -dy

                slope = (dx, dy)

                if slope not in freq:
                    freq[slope] = 1
                else:
                    freq[slope] += 1

            if freq:
                ans = max(ans, max(freq.values()) + 1)

        return ans
```

## 📊 Complexity Analysis

* **Time Complexity:** `O(n² log n)`
* **Space Complexity:** `O(n)`

The algorithm checks every pair of points, and `gcd()` takes logarithmic time.

## 🧠 Key Concepts

* Hash Map
* GCD
* Slope Normalization
* Geometry
* Brute Force

## 🏷️ Difficulty

**Hard**

## 🔗 LeetCode

[Max Points on a Line](https://leetcode.com/problems/max-points-on-a-line/)
