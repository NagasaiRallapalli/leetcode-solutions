# Sort Array By Parity

![LeetCode](https://img.shields.io/badge/LeetCode-905-orange)
![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## 📌 Problem

Given an integer array `nums`, move all even integers to the beginning of the array, followed by all odd integers. The relative order of the elements does not matter.

Return the rearranged array.

## 💡 Example

**Input:**

```python
nums = [3, 1, 2, 4]
```

**Output:**

```python
[2, 4, 3, 1]
```

**Explanation:** Even numbers `2` and `4` appear first, followed by odd numbers `3` and `1`.

## 🚀 Approach

1. Create two empty lists, `a` and `b`.
2. Iterate through each number in `nums`.
3. If the number is even (`i % 2 == 0`), append it to `a`.
4. Otherwise, append it to `b`.
5. Return `a + b` to place all even numbers before the odd numbers.

## 💻 Solution

```python
class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        a = []
        b = []
        for i in nums:
            if i % 2 == 0:
                a.append(i)
            else:
                b.append(i)
        return a + b
```

## 📊 Complexity Analysis

* **Time Complexity:** `O(n)` — Each element is processed once.
* **Space Complexity:** `O(n)` — Two lists store the even and odd elements.

## 🧠 Key Concepts

* Arrays
* Modulo operator (`%`)
* Lists
* Array traversal

## 🏷️ Difficulty

Easy

## 🔗 LeetCode

[Sort Array By Parity — LeetCode 905](https://leetcode.com/problems/sort-array-by-parity/)
