# Jump Game

[![LeetCode](https://img.shields.io/badge/LeetCode-Jump%20Game-orange?style=for-the-badge&logo=leetcode&logoColor=white)](https://leetcode.com/problems/jump-game/)
[![Difficulty](https://img.shields.io/badge/Difficulty-Medium-orange?style=for-the-badge)]()
[![Language](https://img.shields.io/badge/Language-Python-blue?style=for-the-badge&logo=python&logoColor=white)]()

---

## 📌 Problem Statement

You are given an integer array `nums`.

You are initially positioned at the first index.

Each element represents the maximum jump length at that position.

Return `True` if you can reach the last index. Otherwise, return `False`.

---

## 💡 Example

### Input

```text
nums = [2,3,1,1,4]
```

### Output

```text
True
```

### Explanation

Starting from index `0`, we can jump to index `1` and then reach the last index.

---

## 🚀 Approach

This solution uses a **Greedy approach**.

1. Start from the last index.
2. Traverse the array from right to left.
3. Check whether the current index can reach the target index.
4. If it can reach the target, make the current index the new target.
5. Finally, if the target becomes index `0`, the last index is reachable.

---

## 💻 Solution

```python
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums) - 1

        for i in range(n, -1, -1):
            if i + nums[i] >= n:
                n = i

        return n == 0
```

---

## 📊 Complexity Analysis

| Complexity | Value |
|------------|-------|
| **Time Complexity** | **O(n)** |
| **Space Complexity** | **O(1)** |

### ⏱️ Time Complexity

The array is traversed once from right to left.

**O(n)**

### 💾 Space Complexity

Only one extra variable is used.

**O(1)**

---

## 🧠 Key Concepts

- Arrays
- Greedy Algorithm
- Backward Traversal
- Reachability

---

## 🏷️ Difficulty

**Medium** 🟡

---

## 🔗 LeetCode

https://leetcode.com/problems/jump-game/