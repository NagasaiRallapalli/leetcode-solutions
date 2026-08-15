# Merge Sorted Array

[![LeetCode](https://img.shields.io/badge/LeetCode-Merge%20Sorted%20Array-orange?style=for-the-badge&logo=leetcode&logoColor=white)](https://leetcode.com/problems/merge-sorted-array/)
[![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green?style=for-the-badge)]()
[![Language](https://img.shields.io/badge/Language-Python-blue?style=for-the-badge&logo=python&logoColor=white)]()

---

## 📌 Problem Statement

You are given two sorted integer arrays `nums1` and `nums2`.

Merge `nums2` into `nums1` as one sorted array.

The first `m` elements of `nums1` contain the actual values, while the remaining elements are empty space represented by `0`.

---

## 💡 Example

### Input

```text
nums1 = [1,2,3,0,0,0]
m = 3

nums2 = [2,5,6]
n = 3
```

### Output

```text
[1,2,2,3,5,6]
```

### Explanation

Both arrays are already sorted.

We compare the elements from both arrays and add the smaller element to the result.

---

## 🚀 Approach

This solution uses the **Two Pointer** approach.

1. Create an empty list `c`.
2. Use `low` to point to the current element in `nums1`.
3. Use `high` to point to the current element in `nums2`.
4. Compare both elements.
5. Add the smaller element to `c`.
6. Add the remaining elements from either array.
7. Copy the merged result back into `nums1`.

---

## 💻 Solution

```python
class Solution(object):
    def merge(self, a, m, b, n):
        c = []
        low = 0
        high = 0

        while low < m and high < n:
            if a[low] < b[high]:
                c.append(a[low])
                low += 1
            else:
                c.append(b[high])
                high += 1

        while low < m:
            c.append(a[low])
            low += 1

        while high < n:
            c.append(b[high])
            high += 1

        for i in range(len(c)):
            a[i] = c[i]
```

---

## 📊 Complexity Analysis

| Complexity | Value |
|------------|-------|
| **Time Complexity** | **O(m + n)** |
| **Space Complexity** | **O(m + n)** |

### ⏱️ Time Complexity

Each element from both arrays is processed once.

**O(m + n)**

### 💾 Space Complexity

The additional list `c` stores all merged elements.

**O(m + n)**

---

## 🧠 Key Concepts

- Arrays
- Two Pointers
- Sorting
- Merging
- Array Traversal

---

## 🏷️ Difficulty

**Easy** 🟢

---

## 🔗 LeetCode

https://leetcode.com/problems/merge-sorted-array/