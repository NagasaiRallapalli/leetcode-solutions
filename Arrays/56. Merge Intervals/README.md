# Merge Intervals

[![LeetCode](https://img.shields.io/badge/LeetCode-Merge%20Intervals-orange?style=for-the-badge&logo=leetcode&logoColor=white)](https://leetcode.com/problems/merge-intervals/)
[![Difficulty](https://img.shields.io/badge/Difficulty-Medium-orange?style=for-the-badge)]()
[![Language](https://img.shields.io/badge/Language-Python-blue?style=for-the-badge&logo=python&logoColor=white)]()

---

## 📌 Problem Statement

You are given an array of intervals where `intervals[i] = [starti, endi]`.

Merge all overlapping intervals and return an array of the non-overlapping intervals that cover all the intervals in the input.

---

## 💡 Example

### Input

```text
intervals = [[1,3],[2,6],[8,10],[15,18]]
```

### Output

```text
[[1,6],[8,10],[15,18]]
```

### Explanation

The intervals `[1,3]` and `[2,6]` overlap, so they are merged into `[1,6]`.

---

## 🚀 Approach

This solution uses **Sorting and Greedy**.

1. Sort the intervals based on their starting value.
2. Create an empty list `a` to store the merged intervals.
3. Traverse each interval.
4. If there is no overlap, add the interval to `a`.
5. If the intervals overlap, update the ending value of the last interval.
6. Return the merged intervals.

---

## 💻 Solution

```python
class Solution(object):
    def merge(self, intervals):
        intervals.sort(key=lambda x:x[0])
        a=[]

        for i in intervals:
            if not a or a[-1][1]<i[0]:
                a.append(i)
            else:
                a[-1][1]=max(a[-1][1],i[1])

        return a
```

---

## 📊 Complexity Analysis

| Complexity | Value |
|------------|-------|
| **Time Complexity** | **O(n log n)** |
| **Space Complexity** | **O(n)** |

### ⏱️ Time Complexity

Sorting the intervals takes **O(n log n)** time.

The intervals are then traversed once.

**Overall: O(n log n)**

### 💾 Space Complexity

The result list can contain up to `n` intervals.

**O(n)**

---

## 🧠 Key Concepts

- Arrays
- Sorting
- Greedy Algorithm
- Intervals
- Merging

---

## 🏷️ Difficulty

**Medium** 🟡

---

## 🔗 LeetCode

https://leetcode.com/problems/merge-intervals/