# Rotate Array

[![LeetCode](https://img.shields.io/badge/LeetCode-Rotate%20Array-orange?style=for-the-badge\&logo=leetcode\&logoColor=white)](https://leetcode.com/problems/rotate-array/)

[![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow?style=for-the-badge)]()

[![Language](https://img.shields.io/badge/Language-Python-blue?style=for-the-badge\&logo=python\&logoColor=white)]()

---

## 📌 Problem Statement

You are given an integer array `nums`.

Rotate the array to the right by `k` steps, where `k` is non-negative.

---

## 💡 Example

### Input

```text
nums = [1,2,3,4,5,6,7]

k = 3
```

### Output

```text
[5,6,7,1,2,3,4]
```

### Explanation

The array is rotated to the right by `3` positions.

The last `3` elements `[5,6,7]` are moved to the beginning of the array.

---

## 🚀 Approach

This solution uses **Array Slicing**.

1. Find the length of the array `n`.
2. Use `k = k % n` to handle cases where `k` is greater than the array length.
3. Take the last `k` elements using `nums[-k:]`.
4. Take the remaining elements using `nums[:-k]`.
5. Combine both parts and assign them back to `nums`.

---

## 💻 Solution

```python
class Solution(object):

    def rotate(self, nums, k):

        n = len(nums)

        k = k % n

        nums[:] = nums[-k:] + nums[:-k]
```

---

## 📊 Complexity Analysis

| Complexity           | Value    |
| -------------------- | -------- |
| **Time Complexity**  | **O(n)** |
| **Space Complexity** | **O(n)** |

### ⏱️ Time Complexity

Array slicing processes the elements of the array.

**O(n)**

### 💾 Space Complexity

The slicing operation creates new lists containing the array elements.

**O(n)**

---

## 🧠 Key Concepts

* Arrays
* Array Slicing
* Modulo
* List Manipulation
* Array Rotation

---

## 🏷️ Difficulty

**Medium** 🟡

---

## 🔗 LeetCode

https://leetcode.com/problems/rotate-array/
