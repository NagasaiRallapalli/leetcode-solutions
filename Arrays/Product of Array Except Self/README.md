# Product of Array Except Self

[![LeetCode](https://img.shields.io/badge/LeetCode-Product%20of%20Array%20Except%20Self-orange?style=for-the-badge&logo=leetcode&logoColor=white)](https://leetcode.com/problems/product-of-array-except-self/)
[![Difficulty](https://img.shields.io/badge/Difficulty-Medium-orange?style=for-the-badge)]()
[![Language](https://img.shields.io/badge/Language-Python-blue?style=for-the-badge&logo=python&logoColor=white)]()

---

## 📌 Problem Statement

Given an integer array `nums`, return an array `result` such that:

```text
result[i] = product of all elements of nums except nums[i]
```

The solution should run in **O(n)** time and should not use division.

---

## 💡 Example

### Input

```text
nums = [1,2,3,4]
```

### Output

```text
[24,12,8,6]
```

### Explanation

```text
1 → 2 × 3 × 4 = 24
2 → 1 × 3 × 4 = 12
3 → 1 × 2 × 4 = 8
4 → 1 × 2 × 3 = 6
```

---

## 🚀 Approach

This solution uses **Prefix Product** and **Suffix Product**.

### Step 1: Prefix Product

For every index, store the product of all elements to its left.

```text
nums = [1, 2, 3, 4]

result = [1, 1, 2, 6]
```

### Step 2: Suffix Product

Traverse from right to left and multiply the suffix product with the existing prefix product.

```text
result = [24, 12, 8, 6]
```

This allows us to calculate the product except self without using division.

---

## 💻 Solution

```python
class Solution:
    def productExceptSelf(self, nums):
        n = len(nums)
        result = [1] * n

        prefix_product = 1

        for i in range(n):
            result[i] = prefix_product
            prefix_product *= nums[i]

        suffix_product = 1

        for i in range(n - 1, -1, -1):
            result[i] *= suffix_product
            suffix_product *= nums[i]

        return result
```

---

## 📊 Complexity Analysis

| Complexity | Value |
|------------|-------|
| **Time Complexity** | **O(n)** |
| **Space Complexity** | **O(1)** extra space |

The `result` array is considered the output array, so it is not counted as extra space.

---

## 🧠 Key Concepts

- Arrays
- Prefix Product
- Suffix Product
- Two Passes
- Space Optimization

---

## 🏷️ Difficulty

**Medium** 🟡

---

## 🔗 LeetCode

https://leetcode.com/problems/product-of-array-except-self/