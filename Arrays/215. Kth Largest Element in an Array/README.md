# Kth Largest Element in an Array

[![LeetCode](https://img.shields.io/badge/LeetCode-Kth%20Largest%20Element%20in%20an%20Array-orange?style=for-the-badge&logo=leetcode&logoColor=white)](https://leetcode.com/problems/kth-largest-element-in-an-array/)
[![Difficulty](https://img.shields.io/badge/Difficulty-Medium-orange?style=for-the-badge)]()
[![Language](https://img.shields.io/badge/Language-Python-blue?style=for-the-badge&logo=python&logoColor=white)]()

---

## 📌 Problem Statement

Given an integer array `nums` and an integer `k`, return the `kth` largest element in the array.

The kth largest element is based on sorted order, not the kth distinct element.

---

## 💡 Example

### Input

```text
nums = [3,2,1,5,6,4]
k = 2
```

### Output

```text
5
```

### Explanation

After sorting:

```text
[1,2,3,4,5,6]
```

Reverse the array:

```text
[6,5,4,3,2,1]
```

The 2nd largest element is:

```text
5
```

---

## 🚀 Approach

This solution uses **Sorting** and **Array Reversal**.

1. Sort the array in ascending order.
2. Reverse the sorted array using slicing.
3. Access the element at index `k - 1`.
4. Return that element as the kth largest value.

---

## 💻 Solution

```python
class Solution(object):
    def findKthLargest(self, nums, k):
        nums.sort()
        a = nums[::-1]
        return a[k-1]
```

---

## 📊 Complexity Analysis

| Complexity | Value |
|------------|-------|
| **Time Complexity** | **O(n log n)** |
| **Space Complexity** | **O(n)** |

### ⏱️ Time Complexity

Sorting the array takes:

**O(n log n)**

Reversing using `nums[::-1]` takes:

**O(n)**

Therefore, overall:

**O(n log n)**

### 💾 Space Complexity

`nums[::-1]` creates a new reversed list containing `n` elements.

Therefore:

**O(n)**

---

## 🧠 Key Concepts

- Arrays
- Sorting
- Array Slicing
- Reverse Traversal
- Kth Largest Element

---

## 🏷️ Difficulty

**Medium** 🟡

---

## 🔗 LeetCode

https://leetcode.com/problems/kth-largest-element-in-an-array/