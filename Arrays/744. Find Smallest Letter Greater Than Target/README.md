# Find Smallest Letter Greater Than Target

![LeetCode](https://img.shields.io/badge/LeetCode-744-orange)
![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## 📌 Problem

Given a characters array `letters` that is sorted in non-decreasing order and a character `target`, return the smallest character in `letters` that is lexicographically greater than `target`.

If there is no such character, return the first character in `letters`.

### Example

**Input:**

```text
letters = ["c","f","j"]
target = "a"
```

**Output:**

```text
"c"
```

**Explanation:**

`"c"` is the smallest character that is greater than `"a"`.

## 🚀 Approach

We use a **Linear Search** approach.

* Traverse the `letters` array from left to right.
* If the current character is greater than `target`, return that character immediately.
* Since the array is sorted, the first character greater than `target` is the smallest valid answer.
* If no character is greater than `target`, return the first character of the array because the array is circular.

## 💻 Solution

```python
class Solution:

    def nextGreatestLetter(self, letters: List[str], target: str) -> str:

        for i in letters:

            if i > target:

                return i

                break

        return letters[0]
```

## 📊 Complexity Analysis

* **Time Complexity:** `O(n)`
* **Space Complexity:** `O(1)`

We may need to traverse the entire array when no character is greater than `target`.

## 🧠 Key Concepts

* Linear Search
* Array
* String Comparison
* Sorted Array
* Circular Array

## 🏷️ Difficulty

**Easy**

## 🔗 LeetCode

[Find Smallest Letter Greater Than Target](https://leetcode.com/problems/find-smallest-letter-greater-than-target/)
