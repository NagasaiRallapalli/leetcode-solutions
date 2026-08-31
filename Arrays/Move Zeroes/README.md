# Move Zeroes

[![LeetCode](https://img.shields.io/badge/LeetCode-Move%20Zeroes-orange?style=for-the-badge&logo=leetcode&logoColor=white)](https://leetcode.com/problems/move-zeroes/)
[![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green?style=for-the-badge)]()
[![Language](https://img.shields.io/badge/Language-Python-blue?style=for-the-badge&logo=python&logoColor=white)]()

---

## 📌 Problem Statement

Given an integer array `nums`, move all `0`s to the end of the array while maintaining the relative order of the non-zero elements.

The operation must be performed **in-place**.

---

## 💡 Example

### Input

```text
nums = [0,1,0,3,12]
```

### Output

```text
[1,3,12,0,0]
```

---

## 🚀 Approach

This solution uses a **Two Pointer** approach.

- `i` traverses the array.
- `count` keeps track of the position where the next non-zero element should be placed.
- Whenever a non-zero element is found, swap it with `nums[count]`.
- Increment `count`.

This moves all non-zero elements to the front while automatically moving zeroes towards the end.

---

## 💻 Solution

```python
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        count = 0

        for i in range(len(nums)):
            if nums[i] != 0:
                nums[count], nums[i] = nums[i], nums[count]
                count += 1
```

---

## 📊 Complexity Analysis

| Complexity | Value |
|------------|-------|
| **Time Complexity** | **O(n)** |
| **Space Complexity** | **O(1)** |

---

## 🧠 Key Concepts

- Arrays
- Two Pointers
- In-Place Modification
- Swapping
- Array Traversal

---

## 🏷️ Difficulty

**Easy** 🟢

---

## 🔗 LeetCode

https://leetcode.com/problems/move-zeroes/