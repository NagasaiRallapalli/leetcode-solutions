# Longest Consecutive Sequence

[![LeetCode](https://img.shields.io/badge/LeetCode-Longest%20Consecutive%20Sequence-orange)](https://leetcode.com/problems/longest-consecutive-sequence/)

[![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)](https://leetcode.com/problems/longest-consecutive-sequence/)

## 📌 Problem

Given an unsorted array of integers `nums`, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in **O(n)** time.

---

## 💡 Example

### Input

```text
nums = [100,4,200,1,3,2]
```

### Output

```text
4
```

### Explanation

The longest consecutive sequence is:

```text
[1,2,3,4]
```

Therefore, the length of the longest consecutive sequence is **4**.

---

## 🚀 Approach

We use **Set + Sorting** to solve the problem.

1. If the array is empty, return `0`.
2. Convert the array into a `set` to remove duplicate elements.
3. Convert the set back into a list.
4. Sort the list in ascending order.
5. Initialize:

   * `count = 1` to track the current consecutive sequence.
   * `max_sum = 1` to store the longest sequence found.
6. Traverse the sorted array.
7. Compare the current element with the next element:

   * If the difference is `1`, increase `count`.
   * Otherwise, update `max_sum` and reset `count` to `1`.
8. After the loop, update `max_sum` one final time.
9. Return `max_sum`.

---

## 💻 Solution

```python
class Solution:

    def longestConsecutive(self, nums: List[int]) -> int:

        if len(nums) == 0:
            return 0

        nums = list(set(nums))
        nums.sort()

        count = 1
        max_sum = 1

        for i in range(len(nums) - 1):

            if nums[i + 1] - nums[i] == 1:
                count += 1

            else:
                max_sum = max(max_sum, count)
                count = 1

        max_sum = max(max_sum, count)

        return max_sum
```

---

## 📊 Complexity Analysis

| Complexity       | Value          |
| ---------------- | -------------- |
| Time Complexity  | **O(n log n)** |
| Space Complexity | **O(n)**       |

### Time Complexity

**O(n log n)** because after removing duplicates, we sort the array. Sorting takes **O(n log n)** time.

### Space Complexity

**O(n)** because we use a `set` to remove duplicate elements and create a new list.

---

## 🧠 Key Concepts

* Arrays
* Sets
* Sorting
* Consecutive Sequence
* Duplicate Removal
* Traversal

---

## 🏷️ Difficulty

**Medium**

---

## 🔗 LeetCode

[View Problem on LeetCode](https://leetcode.com/problems/longest-consecutive-sequence/)
