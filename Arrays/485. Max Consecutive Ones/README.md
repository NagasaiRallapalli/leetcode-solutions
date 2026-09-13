# Max Consecutive Ones

![LeetCode](https://img.shields.io/badge/LeetCode-485-orange)
![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## 📌 Problem

Given a binary array `nums`, return the maximum number of consecutive `1`s in the array.

### Example

**Input:**

```text
nums = [1,1,0,1,1,1]
```

**Output:**

```text
3
```

**Explanation:**

The consecutive groups of `1`s are:

```text
[1,1] → 2
[1,1,1] → 3
```

The maximum number of consecutive `1`s is `3`.

---

## 🚀 Approach

This solution uses two variables:

* `count` → keeps track of the current consecutive `1`s.
* `max_ones` → stores the maximum consecutive `1`s found so far.

Steps:

1. Traverse every element in `nums`.
2. If the element is `1`, increment `count`.
3. If the element is `0`, compare `count` with `max_ones` and reset `count` to `0`.
4. After the loop, compare one final time because the array may end with `1`s.
5. Return the maximum value.

### Example

For:

```text
nums = [1,1,0,1,1,1]
```

The values of `count` change as:

```text
1 → 2 → 0 → 1 → 2 → 3
```

The maximum is:

```text
3
```

---

## 💻 Solution

```python
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:

        count = 0

        max_ones = 0

        for i in nums:

            if i == 1:

                count += 1

            else:

                max_ones = max(count, max_ones)

                count = 0

        return max(count, max_ones)
```

---

## 📊 Complexity Analysis

Let `n` be the length of `nums`.

| Complexity | Analysis |
| ---------- | -------- |
| Time       | `O(n)`   |
| Space      | `O(1)`   |

Each element is visited exactly once, and only two variables are used.

---

## 🧠 Key Concepts

* Array traversal
* Consecutive elements
* Counting
* `max()` function
* Iterative approach

---

## 🏷️ Difficulty

**Easy**

---

## 🔗 LeetCode

[Max Consecutive Ones](https://leetcode.com/problems/max-consecutive-ones/)
