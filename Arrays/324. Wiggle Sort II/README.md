# Wiggle Sort II

![LeetCode](https://img.shields.io/badge/LeetCode-324-orange)
![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## 📌 Problem

Given an integer array `nums`, reorder it such that:

```text
nums[0] < nums[1] > nums[2] < nums[3] ...
```

The rearrangement should be done in-place.

### Example

**Input:**

```text
nums = [1,5,1,1,6,4]
```

**Output:**

```text
[1,6,1,5,1,4]
```

The output satisfies:

```text
1 < 6 > 1 < 5 > 1 < 4
```

## 🚀 Approach

We first sort the array and divide the elements into two parts.

* `low` points to the end of the smaller half.
* `high` points to the end of the larger half.
* At even indices, place elements from the smaller half.
* At odd indices, place elements from the larger half.
* Both halves are filled from right to left to help maintain the wiggle pattern, especially when duplicate values exist.

## 💻 Solution

```python
class Solution:

    def wiggleSort(self, nums: list[int]) -> None:

        a = sorted(nums)

        n = len(nums)

        low = (n + 1) // 2 - 1

        high = n - 1

        for i in range(n):

            if i % 2 == 0:

                nums[i] = a[low]

                low -= 1

            else:

                nums[i] = a[high]

                high -= 1
```

## 📊 Complexity Analysis

* **Time Complexity:** `O(n log n)`
* **Space Complexity:** `O(n)`

Sorting takes `O(n log n)` time, and `sorted(nums)` creates an additional array of size `n`.

## 🧠 Key Concepts

* Sorting
* Two Pointers
* Array
* Even and Odd Indices
* Greedy Arrangement

## 🏷️ Difficulty

**Medium**

## 🔗 LeetCode

[Wiggle Sort II](https://leetcode.com/problems/wiggle-sort-ii/)
