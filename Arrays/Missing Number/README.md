# Missing Number

[![LeetCode](https://img.shields.io/badge/LeetCode-Missing%20Number-orange?style=for-the-badge&logo=leetcode&logoColor=white)](https://leetcode.com/problems/missing-number/)
[![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green?style=for-the-badge)]()
[![Language](https://img.shields.io/badge/Language-Python-blue?style=for-the-badge&logo=python&logoColor=white)]()

---

## 📌 Problem Statement

Given an array `nums` containing `n` distinct numbers in the range `[0, n]`, return the only number in the range that is missing from the array.

---

## 💡 Example

### Input

```text
nums = [3,0,1]
```

### Output

```text
2
```

### Explanation

The numbers from `0` to `3` are:

```text
[0,1,2,3]
```

The number `2` is missing from the array.

---

## 🚀 Approach

This solution uses the **mathematical sum formula**.

The sum of numbers from `0` to `n` is:

```text
n × (n + 1) / 2
```

1. Find the length of the array.
2. Calculate the expected sum of numbers from `0` to `n`.
3. Calculate the actual sum of the elements using `sum()`.
4. The difference between the expected sum and actual sum gives the missing number.

---

## 💻 Solution

```python
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        total_length = len(nums)

        missing = (total_length * (total_length + 1)) // 2

        total_sum = sum(nums)

        return abs(total_sum - missing)
```

---

## 📊 Complexity Analysis

| Complexity | Value |
|------------|-------|
| **Time Complexity** | **O(n)** |
| **Space Complexity** | **O(1)** |

### ⏱️ Time Complexity

The `sum()` function traverses the array once.

**O(n)**

### 💾 Space Complexity

No additional data structure is used.

**O(1)**

---

## 🧠 Key Concepts

- Arrays
- Mathematical Formula
- Array Traversal
- Sum Calculation

---

## 🏷️ Difficulty

**Easy** 🟢

---

## 🔗 LeetCode

https://leetcode.com/problems/missing-number/