# Container With Most Water

[![LeetCode](https://img.shields.io/badge/LeetCode-Container%20With%20Most%20Water-orange?style=for-the-badge&logo=leetcode&logoColor=white)](https://leetcode.com/problems/container-with-most-water/)
[![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow?style=for-the-badge)](https://leetcode.com/problems/container-with-most-water/)
[![Language](https://img.shields.io/badge/Language-Python-blue?style=for-the-badge&logo=python&logoColor=white)]()

---

# 📌 Problem Statement

Given an integer array `height`, where each element represents the height of a vertical line, find two lines that together with the x-axis form a container such that the container holds the maximum amount of water.

Return the maximum amount of water the container can store.

---

# 💡 Example

### Input

```text
height = [1,8,6,2,5,4,8,3,7]
```

### Output

```text
49
```

---

# 🚀 Approach

This solution uses the **Two Pointers** technique.

1. Place one pointer at the beginning and another at the end.
2. Calculate the area formed by the two lines.
3. Update the maximum area.
4. Move the pointer with the smaller height inward.
5. Continue until both pointers meet.

This approach efficiently finds the maximum water container in linear time.

---

# 💻 Solution

```python
class Solution(object):
    def maxArea(self, height):
        l, r = 0, len(height) - 1
        m = 0

        while l < r:
            h = min(height[l], height[r])
            w = r - l
            m = max(m, h * w)

            if height[l] < height[r]:
                l += 1
            else:
                r -= 1

        return m
```

---

# 📊 Complexity Analysis

| Complexity | Value |
|------------|-------|
| **Time Complexity** | **O(n)** |
| **Space Complexity** | **O(1)** |

---

# 🧠 Key Concepts

- Arrays
- Two Pointers
- Greedy

---

# 🏷️ Difficulty

**Medium** 🟡

---

# 🔗 LeetCode

https://leetcode.com/problems/container-with-most-water/