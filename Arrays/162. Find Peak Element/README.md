# Find Peak Element

[![LeetCode](https://img.shields.io/badge/LeetCode-Find%20Peak%20Element-orange)](https://leetcode.com/problems/find-peak-element/)

[![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)](https://leetcode.com/problems/find-peak-element/)

## 📌 Problem

A peak element is an element that is strictly greater than its neighbors.

Given an integer array `nums`, return the index of a peak element.

You may imagine that `nums[-1] = nums[n] = -∞`.

You must solve the problem in **O(log n)** time.

---

## 💡 Example

### Input

```text
nums = [1,2,3,1]
```

### Output

```text
2
```

### Explanation

The element `3` at index `2` is greater than both its neighbors `2` and `1`.

Therefore, index `2` is a valid peak element.

---

## 🚀 Approach

We use a **Binary Search** approach.

1. Initialize `low = 0` and `high = len(nums) - 1`.

2. Find the middle index:

   `mid = (low + high) // 2`

3. Compare `nums[mid]` with `nums[mid + 1]`.

4. If `nums[mid] > nums[mid + 1]`, a peak exists at `mid` or on the left side.

   So, set:

   `high = mid`

5. Otherwise, `nums[mid] < nums[mid + 1]`, which means the array is increasing towards the right.

   So, set:

   `low = mid + 1`

6. Continue the Binary Search until `low == high`.

7. Return `low` as the index of the peak element.

---

## 💻 Solution

```python
class Solution:

    def findPeakElement(self, nums: List[int]) -> int:

        low = 0
        high = len(nums) - 1

        while low < high:

            mid = (low + high) // 2

            if nums[mid] > nums[mid + 1]:
                high = mid

            else:
                low = mid + 1

        return low
```

---

## 📊 Complexity Analysis

| Complexity       | Value        |
| ---------------- | ------------ |
| Time Complexity  | **O(log n)** |
| Space Complexity | **O(1)**     |

### Time Complexity

**O(log n)** because Binary Search reduces the search space by approximately half in every iteration.

### Space Complexity

**O(1)** because we use only a constant amount of extra space.

---

## 🧠 Key Concepts

* Arrays
* Binary Search
* Searching
* Peak Element
* Divide and Conquer

---

## 🏷️ Difficulty

**Medium**

---

## 🔗 LeetCode

[View Problem on LeetCode](https://leetcode.com/problems/find-peak-element/)
