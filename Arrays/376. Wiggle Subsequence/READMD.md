# Wiggle Subsequence

![LeetCode](https://img.shields.io/badge/LeetCode-376-orange)
![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## 📌 Problem

A wiggle sequence is a sequence where the differences between consecutive numbers strictly alternate between positive and negative.

Given an integer array `nums`, return the length of the longest wiggle subsequence.

### Example

**Input:**

```text
nums = [1,7,4,9,2,5]
```

**Output:**

```text
6
```

**Explanation:**

The entire sequence is a wiggle sequence because the differences alternate:

```text
+6, -3, +5, -7, +3
```

## 🚀 Approach

We first create an array `a` containing the differences between consecutive elements.

* A difference of `0` is ignored.
* We use `low` and `high` pointers to check the differences.
* If consecutive valid differences have opposite signs, the sequence forms a wiggle.
* When the sign changes, increase `count`.
* At the end, add the last valid difference if necessary.

## 💻 Solution

```python
class Solution:

    def wiggleMaxLength(self, nums: List[int]) -> int:

        a = []

        for i in range(len(nums) - 1):

            a.append(nums[i + 1] - nums[i])

        if len(nums) <= 1:

            return len(nums)

        low = 0

        high = 1

        count = 1

        while high < len(a) and low < len(a):

            if a[low] == 0:

                low += 1

                continue

            if (a[low] > 0 and a[high] < 0) or (a[low] < 0 and a[high] > 0):

                count += 1

                low = high

            high += 1

        if low < len(a) and a[low] != 0:

            count += 1

        return count
```

## 📊 Complexity Analysis

* **Time Complexity:** `O(n)`
* **Space Complexity:** `O(n)`

The differences between consecutive elements are stored in an additional array.

## 🧠 Key Concepts

* Two Pointers
* Array
* Subsequence
* Difference Array
* Greedy Approach

## 🏷️ Difficulty

**Medium**

## 🔗 LeetCode

[Wiggle Subsequence](https://leetcode.com/problems/wiggle-subsequence/)