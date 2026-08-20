# Find Minimum in Rotated Sorted Array II

[![LeetCode](https://img.shields.io/badge/LeetCode-Find%20Minimum%20in%20Rotated%20Sorted%20Array%20II-orange?style=for-the-badge&logo=leetcode&logoColor=white)](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array-ii/)
[![Difficulty](https://img.shields.io/badge/Difficulty-Hard-red?style=for-the-badge)]()
[![Language](https://img.shields.io/badge/Language-Python-blue?style=for-the-badge&logo=python&logoColor=white)]()

---

## 📌 Problem Statement

Given a rotated sorted array `nums` that may contain duplicates, return the minimum element in the array.

---

## 💡 Example

### Input

```text
nums = [2,2,2,0,1]
```

### Output

```text
0
```

### Explanation

After sorting the array:

```text
[0,1,2,2,2]
```

The first element is the minimum value.

---

## 🚀 Approach

This solution uses Python's built-in `sort()` method.

1. Sort the given array in ascending order.
2. The smallest element will be at index `0`.
3. Return `nums[0]`.

---

## 💻 Solution

```python
class Solution:
    def findMin(self, nums: List[int]) -> int:
        return min(nums)
```

---

## 📊 Complexity Analysis

| Complexity | Value |
|------------|-------|
| **Time Complexity** | **O(n log n)** |
| **Space Complexity** | **O(1)** auxiliary space |

### ⏱️ Time Complexity

Sorting the array takes:

**O(n log n)**

### 💾 Space Complexity

No additional data structure is explicitly created.

**O(1)** auxiliary space.

---

## 🧠 Key Concepts

- Arrays
- Sorting
- Rotated Sorted Array
- Minimum Element
- Array Traversal

---

## 🏷️ Difficulty

**Hard** 🔴

---

## 🔗 LeetCode

https://leetcode.com/problems/find-minimum-in-rotated-sorted-array-ii/