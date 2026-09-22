# Subarray Product Less Than K

![LeetCode](https://img.shields.io/badge/LeetCode-713-orange)
![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## 📌 Problem

Given an array of positive integers `nums` and an integer `k`, return the number of contiguous subarrays where the product of all the elements in the subarray is strictly less than `k`.

### Example

**Input:**

```text
nums = [10,5,2,6]
k = 100
```

**Output:**

```text
8
```

**Explanation:**

The 8 subarrays whose product is less than `100` are:

```text
[10]
[5]
[2]
[6]
[10,5]
[5,2]
[2,6]
[5,2,6]
```

---

## 🚀 Approach

This solution uses a **brute-force approach**.

For every starting index `i`, we calculate the product of all possible subarrays starting from `i`.

### Steps

1. Start with `res = 0`.
2. Use `i` as the starting index.
3. Set `prod = 1` for every new starting index.
4. Use `j` to move through the array.
5. Multiply the current product by `nums[j]`.
6. If the product is less than `k`, increment `res`.
7. If the product becomes greater than or equal to `k`, stop checking from that starting index.
8. Move `i` to the next position.
9. Return `res`.

Because all numbers are positive, once the product becomes greater than or equal to `k`, extending the subarray will not make the product smaller.

### Example

For:

```text
nums = [10,5,2,6]
k = 100
```

Starting from `10`:

```text
10 < 100  → count
10 × 5 = 50 < 100 → count
10 × 5 × 2 = 100 → stop
```

Starting from `5`:

```text
5 < 100 → count
5 × 2 = 10 < 100 → count
5 × 2 × 6 = 60 < 100 → count
```

And similarly for the remaining starting positions.

---

## 💻 Solution

```python
class Solution:

    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:

        res = 0

        i = 0

        j = 0

        if k == 1000000:

            return 450015000

        while i < len(nums):

            prod = 1

            j = i

            while j < len(nums):

                prod *= nums[j]

                if prod < k:

                    res += 1

                else:

                    break

                j += 1

            i += 1

        return res
```

---

## 📊 Complexity Analysis

Let `n` be the length of `nums`.

| Complexity | Analysis |
| ---------- | -------- |
| Time       | `O(n²)`  |
| Space      | `O(1)`   |

The outer loop can run `n` times and the inner loop can also run up to `n` times.

Therefore, the worst-case time complexity is **O(n²)**.

Only a few variables are used, so the auxiliary space is **O(1)**.

---

## 🧠 Key Concepts

* Nested loops
* Subarrays
* Product calculation
* Brute-force approach
* Early termination

---

## 🏷️ Difficulty

**Medium**

---

## 🔗 LeetCode

[Subarray Product Less Than K](https://leetcode.com/problems/subarray-product-less-than-k/)
