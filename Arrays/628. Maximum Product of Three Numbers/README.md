# Maximum Product of Three Numbers

![LeetCode](https://img.shields.io/badge/LeetCode-628-orange)
![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## 📌 Problem

Given an integer array `nums`, find three numbers whose product is maximum and return the maximum product.

### Example

**Input:**

```text
nums = [1,2,3]
```

**Output:**

```text
6
```

**Explanation:**

The maximum product is:

```text
1 × 2 × 3 = 6
```

### Example 2

**Input:**

```text
nums = [-1,-2,-3,0]
```

**Output:**

```text
6
```

**Explanation:**

The maximum product is:

```text
(-1) × (-2) × (-3) = -6
```

Actually, the maximum product here is `0` because `0` is greater than `-6`.

---

## 🚀 Approach

This solution first sorts the array.

After sorting:

```text
arr[0], arr[1]
```

are the two smallest numbers, and:

```text
arr[n-3], arr[n-2], arr[n-1]
```

are the three largest numbers.

There are two possible cases for the maximum product:

1. **Three largest numbers**

   ```text
   arr[n-1] × arr[n-2] × arr[n-3]
   ```

2. **Two smallest negative numbers × largest number**

   ```text
   arr[0] × arr[1] × arr[n-1]
   ```

The maximum of these two products is the answer.

### Example

For:

```text
nums = [-10,-10,5,2]
```

After sorting:

```text
[-10,-10,2,5]
```

Three largest:

```text
-10? 
```

The relevant candidates are:

```text
2 × 5 × (-10) = -100
(-10) × (-10) × 5 = 500
```

Therefore, the maximum product is:

```text
500
```

---

## 💻 Solution

```python
class Solution:

    def maximumProduct(self, arr: List[int]) -> int:

        arr.sort()

        n = len(arr)

        return max(arr[n - 1] * arr[n - 2] * arr[n - 3], arr[0] * arr[1] * arr[-1])
```

---

## 📊 Complexity Analysis

Let `n` be the length of the array.

| Complexity | Analysis               |
| ---------- | ---------------------- |
| Time       | `O(n log n)`           |
| Space      | `O(1)` auxiliary space |

The sorting operation takes `O(n log n)` time.

After sorting, accessing the required elements and calculating the products takes `O(1)` time.

---

## 🧠 Key Concepts

* Sorting
* Negative numbers
* Array indexing
* Maximum product
* `max()` function

---

## 🏷️ Difficulty

**Easy**

---

## 🔗 LeetCode

[Maximum Product of Three Numbers](https://leetcode.com/problems/maximum-product-of-three-numbers/)
