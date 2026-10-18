# Array of Doubled Pairs

![LeetCode](https://img.shields.io/badge/LeetCode-954-orange)
![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## 📌 Problem

Given an integer array `arr` of even length, return `True` if the array can be rearranged so that every element `x` can be paired with another element `2 * x`. Otherwise, return `False`.

## 💡 Example

**Input:**
```python
arr = [3, 1, 3, 6]
```

**Output:**
```python
False
```

**Explanation:** The two `3`s cannot both be paired with available `6`s because there is only one `6`.

## 🚀 Approach

1. Create a dictionary `freq` to count the frequency of each number.
2. Store the distinct numbers in a list `a`.
3. Sort the numbers by absolute value using `a.sort(key=abs)`. This helps process smaller absolute values before their doubles.
4. For each number `i`:
   - Skip it if its remaining frequency is `0`.
   - Return `False` if `2 * i` is not present or its frequency is insufficient.
   - Subtract the frequency of `i` from the frequency of `2 * i`.
   - Set the frequency of `i` to `0`.
5. If every number is successfully paired, return `True`.

## 💻 Solution

```python
class Solution:
    def canReorderDoubled(self, arr: List[int]) -> bool:
        freq = {}
        for i in arr:
            if i not in freq:
                freq[i] = 1
            else:
                freq[i] += 1

        a = list(freq.keys())
        a.sort(key = abs)

        for i in a:
            if freq[i] == 0:
                continue
            if 2 * i not in freq:
                return False
            if freq[2 * i] < freq[i]:
                return False
                
            freq[2 * i] -=  freq[i]
            freq[i] = 0
        return True
```

## 📊 Complexity Analysis

Let `n` be the length of `arr` and `k` be the number of distinct values.

- **Time Complexity:** `O(n + k log k)` — Counting frequencies takes `O(n)`, and sorting distinct values takes `O(k log k)`.
- **Space Complexity:** `O(k)` — The frequency dictionary and sorted list store distinct values.

## 🧠 Key Concepts

- Hash maps / dictionaries
- Frequency counting
- Sorting by absolute value
- Greedy algorithm

## 🏷️ Difficulty

Medium

## 🔗 LeetCode

[Array of Doubled Pairs — LeetCode 954](https://leetcode.com/problems/array-of-doubled-pairs/)