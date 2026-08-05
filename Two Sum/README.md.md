# Two Sum

[![LeetCode](https://img.shields.io/badge/LeetCode-Two%20Sum-orange)](https://leetcode.com/problems/two-sum/)
[![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)](https://leetcode.com/problems/two-sum/)

## 📌 Problem

Given an array of integers `nums` and an integer `target`, return the indices of the two numbers such that they add up to `target`.

You may assume that each input has exactly one solution, and you cannot use the same element twice.

---

## 💡 Example

### Input

```text
nums = [2, 7, 11, 15]
target = 9
```

### Output

```text
[0, 1]
```

### Explanation

The numbers at indices `0` and `1` are `2` and `7`.

```text
2 + 7 = 9
```

Therefore, the answer is `[0, 1]`.

---

## 🚀 Approach

We use a **Brute Force** approach.

1. Start with the first element of the array.
2. Compare it with every element after it.
3. Check whether their sum is equal to the target.
4. If the sum equals the target, return their indices.
5. Continue until the required pair is found.

---

## 💻 Solution

```python
class Solution(object):
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
```

---

## 📊 Complexity Analysis

| Complexity | Value |
|------------|-------|
| Time Complexity | **O(n²)** |
| Space Complexity | **O(1)** |

### Time Complexity

**O(n²)** because we use two nested loops to check every possible pair of elements.

### Space Complexity

**O(1)** because we use only a constant amount of extra space.

---

## 🧠 Key Concepts

- Arrays
- Brute Force
- Nested Loops
- Searching
- Indexing

---

## 🏷️ Difficulty

**Easy**

---

## 🔗 LeetCode

[View Problem on LeetCode](https://leetcode.com/problems/two-sum/)
