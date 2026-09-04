# Single Number II

[![LeetCode](https://img.shields.io/badge/LeetCode-Single%20Number%20II-orange?style=for-the-badge&logo=leetcode&logoColor=white)](https://leetcode.com/problems/single-number-ii/)
[![Difficulty](https://img.shields.io/badge/Difficulty-Medium-orange?style=for-the-badge)]()
[![Language](https://img.shields.io/badge/Language-Python-blue?style=for-the-badge&logo=python&logoColor=white)]()

---

## 📌 Problem Statement

Given an integer array `nums` where every element appears three times except for one element, which appears exactly once.

Find and return the element that appears only once.

---

## 💡 Example

### Input

```text
nums = [2,2,3,2]
```

### Output

```text
3
```

### Explanation

The number `2` appears three times, while `3` appears only once.

Therefore, the answer is:

```text
3
```

---

## 🚀 Approach

This solution uses the Python `count()` method.

1. Traverse every element in the array.
2. Count how many times the current element appears.
3. If its count is exactly `1`, return that element.

---

## 💻 Solution

```python
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        for i in nums:
            if nums.count(i) == 1:
                return i
```

---

## 📊 Complexity Analysis

| Complexity | Value |
|------------|-------|
| **Time Complexity** | **O(n²)** |
| **Space Complexity** | **O(1)** |

### ⏱️ Time Complexity

`nums.count(i)` traverses the entire array for every element.

Therefore:

**O(n²)**

### 💾 Space Complexity

No additional data structure is used.

**O(1)**

---

## 🧠 Key Concepts

- Arrays
- Counting
- Array Traversal
- Frequency Counting

---

## 🏷️ Difficulty

**Medium** 🟡

---

## 🔗 LeetCode

https://leetcode.com/problems/single-number-ii/