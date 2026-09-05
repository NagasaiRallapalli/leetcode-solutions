# Plus One

[![LeetCode](https://img.shields.io/badge/LeetCode-Plus%20One-orange?style=for-the-badge&logo=leetcode&logoColor=white)](https://leetcode.com/problems/plus-one/)
[![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green?style=for-the-badge)]()
[![Language](https://img.shields.io/badge/Language-Python-blue?style=for-the-badge&logo=python&logoColor=white)]()

---

## 📌 Problem Statement

You are given a large integer represented as an array of digits, where each `digits[i]` is the digit at that position.

Increment the large integer by one and return the resulting array of digits.

---

## 💡 Example

### Input

```text
digits = [1,2,3]
```

### Output

```text
[1,2,4]
```

### Explanation

The array represents the number `123`.

After adding one:

```text
123 + 1 = 124
```

So the result is `[1,2,4]`.

---

## 🚀 Approach

This solution processes the digits from **right to left**.

1. Start from the last digit.
2. If the digit is less than `9`, increment it and return the array.
3. If the digit is `9`, change it to `0` and continue to the previous digit.
4. If all digits are `9`, add `1` at the beginning.

---

## 💻 Solution

```python
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in range(len(digits)-1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits

            digits[i] = 0

        return [1] + digits
```

---

## 📊 Complexity Analysis

| Complexity | Value |
|------------|-------|
| **Time Complexity** | **O(n)** |
| **Space Complexity** | **O(1)** |

### ⏱️ Time Complexity

The digits are traversed from right to left.

**O(n)**

### 💾 Space Complexity

Only constant extra space is used apart from the returned array.

**O(1)**

---

## 🧠 Key Concepts

- Arrays
- Carry
- Backward Traversal
- Simulation

---

## 🏷️ Difficulty

**Easy** 🟢

---

## 🔗 LeetCode

https://leetcode.com/problems/plus-one/