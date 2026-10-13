# Sort an Array

![LeetCode](https://img.shields.io/badge/LeetCode-912-orange)
![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## 📌 Problem

Given an array of integers `nums`, sort the array in ascending order and return it.

You must solve the problem without using built-in sorting functions in the original problem constraints. However, this README documents the submitted approach using Python's built-in `sort()` method.

## 💡 Example

**Input:**

```python
nums = [5, 2, 3, 1]
```

**Output:**

```python
[1, 2, 3, 5]
```

**Explanation:** The array is sorted in ascending order.

## 🚀 Approach

1. Use Python's built-in `sort()` method to sort `nums` in ascending order.
2. Return the sorted array.

## 💻 Solution

```python
class Solution(object):
    def sortArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums.sort()
        return nums
```

## 📊 Complexity Analysis

* **Time Complexity:** `O(n log n)` on average for Python's Timsort.
* **Space Complexity:** `O(n)` auxiliary space in the worst case for Python's sorting implementation.

## 🧠 Key Concepts

* Arrays
* Sorting
* Python `sort()` method

## 🏷️ Difficulty

Medium

## 🔗 LeetCode

[Sort an Array — LeetCode 912](https://leetcode.com/problems/sort-an-array/)
