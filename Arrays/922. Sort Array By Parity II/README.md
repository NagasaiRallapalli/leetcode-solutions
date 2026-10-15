# Sort Array By Parity II

![LeetCode](https://img.shields.io/badge/LeetCode-922-orange)
![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## 📌 Problem

Given an integer array `nums` containing equal numbers of even and odd integers, rearrange the array so that every even index contains an even number and every odd index contains an odd number.

Return the rearranged array.

## 💡 Example

**Input:**
```python
nums = [4, 2, 5, 7]
```

**Output:**
```python
[4, 5, 2, 7]
```

**Explanation:** Even numbers are placed at even indices (`0`, `2`), and odd numbers are placed at odd indices (`1`, `3`).

## 🚀 Approach

1. Initialize `i = 0` to track even indices and `j = 1` to track odd indices.
2. Move `i` forward by `2` whenever the value at an even index is already even.
3. Move `j` forward by `2` whenever the value at an odd index is already odd.
4. Otherwise, swap `nums[i]` and `nums[j]` to correct both positions.
5. Return the modified array.

## 💻 Solution

```python
class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        i = 0
        j = 1
        while i < len(nums) and j < len(nums):
            if nums[i] % 2 == 0:
                i += 2
            elif nums[j] % 2 == 1:
                j += 2
            else:
                nums[i], nums[j] = nums[j], nums[i]
                i += 2
                j += 2
        return nums
```

## 📊 Complexity Analysis

- **Time Complexity:** `O(n)` — The pointers move forward through the array.
- **Space Complexity:** `O(1)` — The rearrangement is performed in place.

## 🧠 Key Concepts

- Arrays
- Two pointers
- Modulo operator (`%`)
- In-place swapping

## 🏷️ Difficulty

Easy

## 🔗 LeetCode

[Sort Array By Parity II — LeetCode 922](https://leetcode.com/problems/sort-array-by-parity-ii/)