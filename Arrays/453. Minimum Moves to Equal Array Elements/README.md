# Minimum Moves to Equal Array Elements

![LeetCode](https://img.shields.io/badge/LeetCode-453-orange)
![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## 📌 Problem

Given an integer array `nums`, return the minimum number of moves required to make all array elements equal.

In one move, you can increment `n - 1` elements by `1`, where `n` is the size of the array.

## 💡 Example

**Input:**
```python
nums = [1, 2, 3]
```

**Output:**
```python
3
```

**Explanation:**

- Move 1: `[2, 3, 3]`
- Move 2: `[3, 4, 3]`
- Move 3: `[4, 4, 4]`

The minimum number of moves required is `3`.

## 🚀 Approach

1. Find the length of the array using `len(nums)` and store it in `n`.
2. Find the minimum element using `min(nums)`.
3. Calculate the sum of all elements using `sum(nums)`.
4. Apply the formula:

   `Minimum Moves = sum(nums) - (n * min(nums))`

5. Return the result.

**Logic:** Incrementing `n - 1` elements by 1 is equivalent to decreasing the remaining element by 1. So, the optimal approach is to make every element equal to the minimum element.

## 💻 Solution

```python
class Solution:
    def minMoves(self, nums: list[int]) -> int:
        n = len(nums)
        return sum(nums) - (n * min(nums))
```

## 📊 Complexity Analysis

- **Time Complexity:** `O(n)` — Finding the sum and minimum element requires traversing the array.
- **Space Complexity:** `O(1)` — Only one extra variable is used.

## 🧠 Key Concepts

- Arrays
- Minimum element
- Array sum
- Mathematical formula

## 🏷️ Difficulty

Easy

## 🔗 LeetCode

[Minimum Moves to Equal Array Elements — LeetCode 453](https://leetcode.com/problems/minimum-moves-to-equal-array-elements/)