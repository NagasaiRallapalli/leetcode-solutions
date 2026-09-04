# Search in Rotated Sorted Array

[![LeetCode](https://img.shields.io/badge/LeetCode-Search%20in%20Rotated%20Sorted%20Array-orange?style=for-the-badge&logo=leetcode&logoColor=white)](https://leetcode.com/problems/search-in-rotated-sorted-array/)
[![Difficulty](https://img.shields.io/badge/Difficulty-Medium-orange?style=for-the-badge)]()
[![Language](https://img.shields.io/badge/Language-Python-blue?style=for-the-badge&logo=python&logoColor=white)]()

---

## 📌 Problem Statement

Given an integer array `nums` sorted in ascending order and rotated at an unknown position, and an integer `target`, return the index of `target` if it exists in the array.

If `target` does not exist, return `-1`.

---

## 💡 Example

### Input

```text
nums = [4,5,6,7,0,1,2]
target = 0
```

### Output

```text
4
```

---

## 🚀 Approach

This solution uses **Linear Search**.

1. Traverse the array from the first element.
2. Compare every element with the target.
3. If the target is found, return its index.
4. If the loop finishes without finding the target, return `-1`.

---

## 💻 Solution

```python
class Solution(object):
    def search(self, nums, t):
        for i in range(len(nums)):
            if nums[i] == t:
                return i
        return -1
```

---

## 📊 Complexity Analysis

| Complexity | Value |
|------------|-------|
| **Time Complexity** | **O(n)** |
| **Space Complexity** | **O(1)** |

### ⏱️ Time Complexity

In the worst case, we may need to check every element.

**O(n)**

### 💾 Space Complexity

Only a few variables are used and no extra data structure is created.

**O(1)**

---

## 🧠 Key Concepts

- Arrays
- Linear Search
- Array Traversal
- Searching

---

## 🏷️ Difficulty

**Medium** 🟡

---

## 🔗 LeetCode

https://leetcode.com/problems/search-in-rotated-sorted-array/