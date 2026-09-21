# Binary Search

![LeetCode](https://img.shields.io/badge/LeetCode-704-orange)
![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## 📌 Problem

Given a sorted array of integers `nums` and an integer `target`, return the index of `target` if it exists in the array.

If `target` does not exist, return `-1`.

You must write an algorithm with `O(log n)` runtime complexity.

### Example

**Input:**

```text
nums = [-1,0,3,5,9,12]
target = 9
```

**Output:**

```text
4
```

**Explanation:**

The target `9` is present at index `4`.

### Example 2

**Input:**

```text
nums = [-1,0,3,5,9,12]
target = 2
```

**Output:**

```text
-1
```

**Explanation:**

The target `2` is not present in the array.

---

## 🚀 Approach

This solution uses **Binary Search**.

We maintain two pointers:

* `low` → starting index of the search range.
* `high` → ending index of the search range.

Steps:

1. Calculate the middle index:

   ```text
   mid = (low + high) // 2
   ```
2. If `nums[mid] == target`, return `mid`.
3. If `nums[mid] > target`, search the left half by moving `high`.
4. Otherwise, search the right half by moving `low`.
5. Continue until `low > high`.
6. If the target is not found, return `-1`.

### Example

For:

```text
nums = [-1,0,3,5,9,12]
target = 9
```

First:

```text
low = 0
high = 5
mid = 2
nums[mid] = 3
```

Since `3 < 9`, search the right half.

Next:

```text
low = 3
high = 5
mid = 4
nums[mid] = 9
```

Target found at index `4`.

---

## 💻 Solution

```python
class Solution:

    def search(self, nums: List[int], target: int) -> int:

        low = 0

        high = len(nums) - 1

        while low <= high:

            mid = (low + high) // 2

            if nums[mid] == target:

                return mid

            elif nums[mid] > target:

                high = mid - 1

            else:

                low = mid + 1

        return -1
```

---

## 📊 Complexity Analysis

Let `n` be the length of `nums`.

| Complexity | Analysis   |
| ---------- | ---------- |
| Time       | `O(log n)` |
| Space      | `O(1)`     |

Each iteration eliminates approximately half of the remaining search space.

---

## 🧠 Key Concepts

* Binary Search
* Sorted Array
* Two Pointers
* `low`, `high`, and `mid`
* Iterative approach

---

## 🏷️ Difficulty

**Easy**

---

## 🔗 LeetCode

[Binary Search](https://leetcode.com/problems/binary-search/)
