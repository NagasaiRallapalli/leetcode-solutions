# First Missing Positive

[![LeetCode](https://img.shields.io/badge/LeetCode-First%20Missing%20Positive-orange?style=for-the-badge&logo=leetcode&logoColor=white)](https://leetcode.com/problems/first-missing-positive/)
[![Difficulty](https://img.shields.io/badge/Difficulty-Hard-red?style=for-the-badge)]()
[![Language](https://img.shields.io/badge/Language-Python-blue?style=for-the-badge&logo=python&logoColor=white)]()

---

## 📌 Problem Statement

Given an unsorted integer array `nums`, return the smallest missing positive integer.

The solution should identify the missing positive number from the range starting at `1`.

---

## 💡 Example

### Input

```text
nums = [3,4,-1,1]
```

### Output

```text
2
```

### Explanation

The positive integers start from:

```text
1, 2, 3, 4, ...
```

The number `1` is present, `2` is missing, so the answer is `2`.

---

## 🚀 Approach

This solution uses a **Set** to store all elements of the array.

1. Create a set containing all numbers in `nums`.
2. Start checking positive integers from `1`.
3. If a number is not present in the set, return it.
4. If all numbers from `1` to `n` are present, the answer is `n + 1`.

Using a set provides fast average-case membership checking.

---

## 💻 Solution

```python
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        seen = set(nums)

        for i in range(1, len(nums) + 1):
            if i not in seen:
                return i

        return len(nums) + 1
```

---

## 📊 Complexity Analysis

| Complexity | Value |
|------------|-------|
| **Time Complexity** | **O(n)** average |
| **Space Complexity** | **O(n)** |

---

## 🧠 Key Concepts

- Arrays
- Hash Set
- Membership Checking
- Positive Integers
- Array Traversal

---

## 🏷️ Difficulty

**Hard** 🔴

---

## 🔗 LeetCode

https://leetcode.com/problems/first-missing-positive/