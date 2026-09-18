# Single Element in a Sorted Array

![LeetCode](https://img.shields.io/badge/LeetCode-540-orange)
![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## 📌 Problem

You are given a sorted array `nums` where every element appears exactly twice, except for one element that appears exactly once.

Return the element that appears only once.

### Example

**Input:**

```text
nums = [1,1,2,3,3,4,4,8,8]
```

**Output:**

```text
2
```

**Explanation:**

Every number appears twice except `2`, which appears only once.

---

## 🚀 Approach

This solution uses the **XOR (`^`) operator**.

The important XOR properties are:

```text
a ^ a = 0
a ^ 0 = a
```

So, when we XOR all elements:

* Every duplicate pair cancels out to `0`.
* The single element remains.

### Example

For:

```text
nums = [1,1,2,3,3,4,4]
```

XOR operation:

```text
1 ^ 1 ^ 2 ^ 3 ^ 3 ^ 4 ^ 4
```

Duplicate elements cancel:

```text
0 ^ 2 ^ 0 ^ 0
```

Result:

```text
2
```

Therefore, the single non-duplicate element is `2`.

---

## 💻 Solution

```python
class Solution:

    def singleNonDuplicate(self, nums: List[int]) -> int:

        res = 0

        for i in nums:

            res = res ^ i

        return res
```

---

## 📊 Complexity Analysis

Let `n` be the length of `nums`.

| Complexity | Analysis |
| ---------- | -------- |
| Time       | `O(n)`   |
| Space      | `O(1)`   |

Each element is visited once, and only one extra variable `res` is used.

---

## 🧠 Key Concepts

* XOR
* Bitwise operators
* Duplicate cancellation
* Array traversal

---

## 🏷️ Difficulty

**Medium**

---

## 🔗 LeetCode

[Single Element in a Sorted Array](https://leetcode.com/problems/single-element-in-a-sorted-array/)
