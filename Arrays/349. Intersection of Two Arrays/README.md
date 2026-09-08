# Intersection of Two Arrays

[![LeetCode](https://img.shields.io/badge/LeetCode-Intersection%20of%20Two%20Arrays-orange)](https://leetcode.com/problems/intersection-of-two-arrays/)
[![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)](https://leetcode.com/problems/intersection-of-two-arrays/)

## 📌 Problem

Given two integer arrays `nums1` and `nums2`, return their intersection.

Each element in the result must be **unique**.

---

## 💡 Example

### Input

```text
nums1 = [1, 2, 2, 1]
nums2 = [2, 2]
```

### Output

```text
[2]
```

### Explanation

The common element between `nums1` and `nums2` is `2`.

Since the result must contain unique elements, the output is `[2]`.

---

## 🚀 Approach

We use a **Simple Searching** approach.

1. Create an empty list `a`.
2. Traverse each element in `nums1`.
3. Check whether the element exists in `nums2`.
4. If it exists, add it to `a`.
5. Convert `a` into a set to remove duplicate elements.
6. Convert the set back into a list.

---

## 💻 Solution

```python
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:

        a = []

        for i in nums1:
            if i in nums2:
                a.append(i)

        return list(set(a))
```

---

## 📊 Complexity Analysis

| Complexity       | Value        |
| ---------------- | ------------ |
| Time Complexity  | **O(n × m)** |
| Space Complexity | **O(n)**     |

### Time Complexity

**O(n × m)** because for every element in `nums1`, we search for that element in `nums2`.

### Space Complexity

**O(n)** because we store the common elements in list `a` and remove duplicates using a set.

---

## 🧠 Key Concepts

* Arrays
* Linear Search
* Set
* Duplicate Removal
* Searching

---

## 🏷️ Difficulty

**Easy**

---

## 🔗 LeetCode

[View Problem on LeetCode](https://leetcode.com/problems/intersection-of-two-arrays/)
