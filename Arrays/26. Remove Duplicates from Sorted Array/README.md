# Remove Duplicates from Sorted Array

[![LeetCode](https://img.shields.io/badge/LeetCode-Remove%20Duplicates%20from%20Sorted%20Array-orange?style=for-the-badge&logo=leetcode&logoColor=white)](https://leetcode.com/problems/remove-duplicates-from-sorted-array/)
[![Difficulty](https://img.shields.io/badge/Difficulty-Easy-brightgreen?style=for-the-badge)](https://leetcode.com/problems/remove-duplicates-from-sorted-array/)
[![Language](https://img.shields.io/badge/Language-Python-blue?style=for-the-badge&logo=python&logoColor=white)]()

---

## 📌 Problem Statement

Given a sorted integer array `nums`, remove the duplicates in-place so that each unique element appears only once.

Return the number of unique elements.

---

## 💡 Example

### Input

```text
nums = [1,1,2]
```

### Output

```text
2
```

### Explanation

The first `2` positions contain the unique values:

```text
[1,2,...]
```

---

## 🚀 Approach

This solution uses the **Two Pointer** technique.

1. `j` keeps track of the position of the last unique element.
2. Start `i` from the second element.
3. Compare `arr[i]` with `arr[j]`.
4. If they are different, move `j` forward and copy `arr[i]` to `arr[j]`.
5. Return `j + 1`.

The array is modified **in-place**, so no extra array or set is required.

---

## 💻 Solution

```python
class Solution(object):
    def removeDuplicates(self, arr):
        if len(arr) == 0:
            return 0

        j = 0

        for i in range(1, len(arr)):
            if arr[i] != arr[j]:
                j += 1
                arr[j] = arr[i]

        return j + 1
```

---

## 📊 Complexity Analysis

| Complexity | Value |
|------------|-------|
| **Time Complexity** | **O(n)** |
| **Space Complexity** | **O(1)** |

### ⏱️ Time Complexity

The array is traversed only once.

**O(n)**

### 💾 Space Complexity

No extra data structure is used.

**O(1)**

---

## 🧠 Key Concepts

- Arrays
- Two Pointers
- In-place Modification
- Duplicate Removal

---

## 🏷️ Difficulty

**Easy** 🟢

---

## 🔗 LeetCode

https://leetcode.com/problems/remove-duplicates-from-sorted-array/