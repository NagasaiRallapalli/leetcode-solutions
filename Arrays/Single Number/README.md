# Single Number

[![LeetCode](https://img.shields.io/badge/LeetCode-Single%20Number-orange?style=for-the-badge&logo=leetcode&logoColor=white)](https://leetcode.com/problems/single-number/)
[![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green?style=for-the-badge)]()
[![Language](https://img.shields.io/badge/Language-Python-blue?style=for-the-badge&logo=python&logoColor=white)]()

---

## 📌 Problem Statement

Given a non-empty array of integers `nums`, every element appears twice except for one element.

Find and return the element that appears only once.

You must solve the problem with **linear runtime complexity** and use **constant extra space**.

---

## 💡 Example

### Input

```text
nums = [4,1,2,1,2]
```

### Output

```text
4
```

### Explanation

Every number appears twice except `4`.

---

## 🚀 Approach

This solution uses the **XOR (^)** operator.

Important XOR properties:

```text
a ^ a = 0
a ^ 0 = a
```

Since every number except one appears twice, the duplicate numbers cancel each other out.

For example:

```text
4 ^ 1 ^ 2 ^ 1 ^ 2
```

The pairs cancel:

```text
4 ^ (1 ^ 1) ^ (2 ^ 2)
= 4 ^ 0 ^ 0
= 4
```

---

## 💻 Solution

```python
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        a = 0

        for i in nums:
            a = a ^ i

        return a
```

---

## 📊 Complexity Analysis

| Complexity | Value |
|------------|-------|
| **Time Complexity** | **O(n)** |
| **Space Complexity** | **O(1)** |

### ⏱️ Time Complexity

Every element is visited exactly once.

**O(n)**

### 💾 Space Complexity

Only one extra variable `a` is used.

**O(1)**

---

## 🧠 Key Concepts

- Arrays
- Bit Manipulation
- XOR
- Linear Traversal

---

## 🏷️ Difficulty

**Easy** 🟢

---

## 🔗 LeetCode

https://leetcode.com/problems/single-number/