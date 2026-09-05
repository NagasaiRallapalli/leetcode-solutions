# Sort Colors

[![LeetCode](https://img.shields.io/badge/LeetCode-Sort%20Colors-orange?style=for-the-badge&logo=leetcode&logoColor=white)](https://leetcode.com/problems/sort-colors/)
[![Difficulty](https://img.shields.io/badge/Difficulty-Medium-orange?style=for-the-badge)]()
[![Language](https://img.shields.io/badge/Language-Python-blue?style=for-the-badge&logo=python&logoColor=white)]()

---

## 📌 Problem Statement

Given an array `nums` containing `0`, `1`, and `2`, sort the array in-place so that objects of the same color are adjacent.

The colors are represented as:

```text
0 → Red
1 → White
2 → Blue
```

---

## 💡 Example

### Input

```text
nums = [2,0,2,1,1,0]
```

### Output

```text
[0,0,1,1,2,2]
```

### Explanation

The array is sorted in ascending order, grouping all `0`s first, followed by `1`s and then `2`s.

---

## 🚀 Approach

This solution uses **Bubble Sort**.

1. Traverse the array using two loops.
2. Compare adjacent elements.
3. If the current element is greater than the next element, swap them.
4. After every pass, the largest unsorted element moves to its correct position.
5. Continue until the entire array is sorted.

---

## 💻 Solution

```python
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        for i in range(len(nums)):
            for j in range(len(nums)-i-1):
                if nums[j] > nums[j+1]:
                    nums[j], nums[j+1] = nums[j+1], nums[j]
```

---

## 📊 Complexity Analysis

| Complexity | Value |
|------------|-------|
| **Time Complexity** | **O(n²)** |
| **Space Complexity** | **O(1)** |

### ⏱️ Time Complexity

Bubble Sort uses nested loops, so in the worst case it takes:

**O(n²)**

### 💾 Space Complexity

Only a temporary swap is used and no extra data structure is required.

**O(1)**

---

## 🧠 Key Concepts

- Arrays
- Sorting
- Bubble Sort
- In-place Sorting
- Swapping

---

## 🏷️ Difficulty

**Medium** 🟡

---

## 🔗 LeetCode

https://leetcode.com/problems/sort-colors/