# Minimum Size Subarray Sum

![LeetCode](https://img.shields.io/badge/LeetCode-209-orange)
![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## 📌 Problem

Given an array of positive integers `nums` and a positive integer `target`, return the minimal length of a contiguous subarray whose sum is greater than or equal to `target`.

If there is no such subarray, return `0`.

### Example

**Input:**

```text
target = 7
nums = [2,3,1,2,4,3]
```

**Output:**

```text
2
```

**Explanation:**

The subarray `[4,3]` has a sum of `7` and has the minimum length of `2`.

## 🚀 Approach

We use the **Sliding Window** technique.

* `i` represents the starting index of the window.
* `j` represents the ending index of the window.
* `total` stores the sum of the current window.
* `count` stores the minimum subarray length found so far.
* Expand the window by adding `nums[j]`.
* When `total >= target`, update the minimum length and shrink the window from the left.
* If no valid subarray is found, return `0`.

## 💻 Solution

```python
class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        n = len(nums)
        count = float('inf')
        total = 0
        i = 0
        for j in range(i, n):
            total += nums[j]
            while total >= target:
                count = min(count, j - i + 1)
                total -= nums[i]
                i += 1
                    
        if count == float('inf'):
            return 0
        return count
```

## 📊 Complexity Analysis

* **Time Complexity:** `O(n)`
* **Space Complexity:** `O(1)`

Each element is added to the window once and removed from the window at most once.

## 🧠 Key Concepts

* Sliding Window
* Two Pointers
* Array
* Subarray
* Prefix Sum Concept

## 🏷️ Difficulty

**Medium**

## 🔗 LeetCode

[Minimum Size Subarray Sum](https://leetcode.com/problems/minimum-size-subarray-sum/)
