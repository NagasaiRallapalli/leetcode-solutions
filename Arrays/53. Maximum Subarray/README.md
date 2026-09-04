# Maximum Subarray

[![LeetCode](https://img.shields.io/badge/LeetCode-Maximum%20Subarray-orange?style=for-the-badge&logo=leetcode&logoColor=white)](https://leetcode.com/problems/maximum-subarray/)
[![Difficulty](https://img.shields.io/badge/Difficulty-Medium-orange?style=for-the-badge)]()
[![Language](https://img.shields.io/badge/Language-Python-blue?style=for-the-badge&logo=python&logoColor=white)]()

---

## 📌 Problem Statement

Given an integer array `nums`, find the subarray with the largest sum and return its sum.

A subarray must contain at least one element.

---

## 💡 Example

### Input

```text
nums = [-2,1,-3,4,-1,2,1,-5,4]
```

### Output

```text
6
```

### Explanation

The subarray:

```text
[4,-1,2,1]
```

has the largest sum:

```text
4 + (-1) + 2 + 1 = 6
```

---

## 🚀 Approach

This solution uses **Kadane's Algorithm**.

1. Initialize `a` and `b` with the first element.
2. For every next element, calculate the maximum between:
   - Starting a new subarray from the current element.
   - Adding the current element to the previous subarray.
3. Store the maximum sum found so far in `a`.
4. Return `a`.

---

## 💻 Solution

```python
class Solution(object):
    def maxSubArray(self, arr):
        a = b = arr[0]

        for i in range(1, len(arr)):
            b = max(arr[i], b + arr[i])
            a = max(a, b)

        return a
```

---

## 📊 Complexity Analysis

| Complexity | Value |
|------------|-------|
| **Time Complexity** | **O(n)** |
| **Space Complexity** | **O(1)** |

### ⏱️ Time Complexity

The array is traversed only once.

**O(n)**

### 💾 Space Complexity

Only two variables are used.

**O(1)**

---

## 🧠 Key Concepts

- Arrays
- Kadane's Algorithm
- Dynamic Programming
- Maximum Subarray
- Array Traversal

---

## 🏷️ Difficulty

**Medium** 🟡

---

## 🔗 LeetCode

https://leetcode.com/problems/maximum-subarray/