# Third Maximum Number

![LeetCode](https://img.shields.io/badge/LeetCode-414-orange)
![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## 📌 Problem

Given an integer array `nums`, return the **third distinct maximum number** in this array.

If the third maximum does not exist, return the maximum number.

A distinct maximum means that duplicate values are counted only once.

### Example 1

**Input:**

```text
nums = [3,2,1]
```

**Output:**

```text
1
```

**Explanation:**

The distinct values are `3, 2, 1`.

* Maximum = `3`
* Second maximum = `2`
* Third maximum = `1`

Therefore, the answer is `1`.

### Example 2

**Input:**

```text
nums = [1,2]
```

**Output:**

```text
2
```

**Explanation:**

There are only two distinct numbers, so we return the maximum number `2`.

---

## 🚀 Approach

This solution uses **set + sorting**.

1. Convert `nums` into a set using `set(nums)` to remove duplicate values.
2. Sort the unique values in ascending order using `sorted()`.
3. If there are fewer than 3 distinct numbers, return the last element `a[-1]`, which is the maximum.
4. Otherwise, return `a[-3]`, which is the third largest distinct number.

### Example

```text
nums = [2,2,3,1]
```

After removing duplicates:

```text
{1,2,3}
```

After sorting:

```text
[1,2,3]
```

The third maximum is:

```text
a[-3] = 1
```

So the output is:

```text
1
```

---

## 💻 Solution

```python
class Solution(object):
    def thirdMax(self, nums):
        a = sorted(set(nums))
        
        if len(a) < 3:
            return a[-1]
        
        return a[-3]
```

---

## 📊 Complexity Analysis

Let `n` be the number of elements in `nums`.

| Complexity | Analysis     |
| ---------- | ------------ |
| Time       | `O(n log n)` |
| Space      | `O(n)`       |

### Why `O(n log n)`?

* `set(nums)` takes `O(n)` time.
* Sorting the unique elements takes `O(n log n)` in the worst case.
* Accessing `a[-1]` or `a[-3]` takes `O(1)`.

Therefore, the overall time complexity is **O(n log n)**.

---

## 🧠 Key Concepts

* Sets
* Removing duplicates
* Sorting
* Negative indexing
* Conditional statements

---

## 🏷️ Difficulty

**Easy**

---

## 🔗 LeetCode

[Third Maximum Number](https://leetcode.com/problems/third-maximum-number/)
