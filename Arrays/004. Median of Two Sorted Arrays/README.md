# Median of Two Sorted Arrays

[![LeetCode](https://img.shields.io/badge/LeetCode-Median%20of%20Two%20Sorted%20Arrays-orange?style=for-the-badge&logo=leetcode&logoColor=white)](https://leetcode.com/problems/median-of-two-sorted-arrays/)
[![Difficulty](https://img.shields.io/badge/Difficulty-Hard-red?style=for-the-badge)](https://leetcode.com/problems/median-of-two-sorted-arrays/)
[![Language](https://img.shields.io/badge/Language-Python-blue?style=for-the-badge&logo=python&logoColor=white)]()

---

# 📌 Problem Statement

Given two sorted arrays `nums1` and `nums2` of size `m` and `n` respectively, return the **median** of the two sorted arrays.

The overall run time complexity should ideally be **O(log(m+n))**.

---

# 💡 Example 1

### Input

```text
nums1 = [1,3]
nums2 = [2]
```

### Output

```text
2.0
```

### Explanation

Merged array:

```text
[1,2,3]
```

Median = **2**

---

# 💡 Example 2

### Input

```text
nums1 = [1,2]
nums2 = [3,4]
```

### Output

```text
2.5
```

### Explanation

Merged array:

```text
[1,2,3,4]
```

Median = **(2 + 3) / 2 = 2.5**

---

# 🚀 Approach

This solution uses a simple and beginner-friendly approach.

1. Merge both input arrays.
2. Sort the merged array.
3. Find the total number of elements.
4. If the size is odd, return the middle element.
5. If the size is even, return the average of the two middle elements.

> **Note:** This solution is easy to understand but does **not** achieve the optimal `O(log(m+n))` time complexity required by the original problem.

---

# 💻 Solution

```python
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        a = nums1 + nums2
        a.sort()
        n = len(a)

        if n % 2 == 1:
            return a[n // 2]
        else:
            return (a[n // 2 - 1] + a[n // 2]) / 2.0
```

---

# 📊 Complexity Analysis

| Complexity | Value |
|------------|-------|
| **Time Complexity** | **O((m+n) log(m+n))** |
| **Space Complexity** | **O(m+n)** |

### ⏱️ Time Complexity

- Merging two arrays takes **O(m+n)**.
- Sorting the merged array takes **O((m+n) log(m+n))**.
- Finding the median takes **O(1)**.

Overall Time Complexity:

**O((m+n) log(m+n))**

### 💾 Space Complexity

An additional array is created to store all elements.

**O(m+n)**

---

# 🧠 Key Concepts

- Arrays
- Sorting
- Merge Arrays
- Median
- Simulation

---

# 🏷️ Difficulty

**Hard** 🔴

---

# 🔗 LeetCode Problem

https://leetcode.com/problems/median-of-two-sorted-arrays/