# Maximum Product Subarray

[![LeetCode](https://img.shields.io/badge/LeetCode-Maximum%20Product%20Subarray-orange?style=for-the-badge\&logo=leetcode\&logoColor=white)](https://leetcode.com/problems/maximum-product-subarray/)
[![Difficulty](https://img.shields.io/badge/Difficulty-Medium-orange?style=for-the-badge)]()
[![Language](https://img.shields.io/badge/Language-Python-blue?style=for-the-badge\&logo=python\&logoColor=white)]()

---

## 📌 Problem Statement

Given an integer array `nums`, find the contiguous subarray that has the largest product and return the product.

A subarray must contain at least one element.

---

## 💡 Example

### Input

```text
nums = [2,3,-2,4]
```

### Output

```text
6
```

### Explanation

The subarray `[2,3]` has the largest product.

```text
2 × 3 = 6
```

Therefore, the answer is:

```text
6
```

---

## 🚀 Approach

This solution keeps track of both the maximum and minimum product ending at the current position.

1. Initialize the maximum product, minimum product, and result with the first element.
2. Traverse the array from the second element.
3. If the current element is negative, swap the maximum and minimum products.
4. Calculate the new maximum product.
5. Calculate the new minimum product.
6. Update the result with the maximum product found so far.

The minimum product is also maintained because multiplying two negative numbers can produce a positive maximum product.

---

## 📊 Complexity Analysis

| Complexity           | Value    |
| -------------------- | -------- |
| **Time Complexity**  | **O(n)** |
| **Space Complexity** | **O(1)** |

### ⏱️ Time Complexity

The array is traversed only once.

Therefore:

**O(n)**

### 💾 Space Complexity

No additional data structure is used.

Only a few variables are maintained.

Therefore:

**O(1)**

---

## 🧠 Key Concepts

* Arrays
* Subarrays
* Maximum Product
* Minimum Product
* Dynamic Programming
* Array Traversal

---

## 🏷️ Difficulty

**Medium** 🟡

---

## 🔗 LeetCode

https://leetcode.com/problems/maximum-product-subarray/
