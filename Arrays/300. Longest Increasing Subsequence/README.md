# Longest Increasing Subsequence

![LeetCode](https://img.shields.io/badge/LeetCode-300-orange)
![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## 📌 Problem

Given an integer array `nums`, return the length of the longest strictly increasing subsequence.

A subsequence is a sequence that can be derived from the array by deleting some or no elements without changing the order of the remaining elements.

### Example

**Input:**

```text
nums = [10,9,2,5,3,7,101,18]
```

**Output:**

```text
4
```

**Explanation:**

One of the longest increasing subsequences is `[2,3,7,101]`, which has a length of `4`.

## 🚀 Approach

We use **Dynamic Programming (DP)**.

* Create a `dp` array where every value is initially `1`.
* `dp[i]` represents the length of the longest increasing subsequence ending at index `i`.
* For every `i`, check all previous indices `j`.
* If `nums[j] < nums[i]`, then `nums[i]` can extend the subsequence ending at `j`.
* Update `dp[i]` using:

```python
dp[i] = max(dp[i], dp[j] + 1)
```

* The answer is the maximum value in `dp`.

## 💻 Solution

```python
class Solution:

    def lengthOfLIS(self, nums: list[int]) -> int:

        dp = [1] * len(nums)

        for i in range(len(nums)):

            for j in range(i):

                if nums[j] < nums[i]:

                    dp[i] = max(dp[i], dp[j] + 1)

        return max(dp)
```

## 📊 Complexity Analysis

* **Time Complexity:** `O(n²)`
* **Space Complexity:** `O(n)`

The nested loops compare each element with the elements before it.

## 🧠 Key Concepts

* Dynamic Programming
* Subsequence
* Array
* Nested Loops

## 🏷️ Difficulty

**Medium**

## 🔗 LeetCode

[Longest Increasing Subsequence](https://leetcode.com/problems/longest-increasing-subsequence/)
