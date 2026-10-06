# 1-bit and 2-bit Characters

![LeetCode](https://img.shields.io/badge/LeetCode-717-orange)
![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## 📌 Problem

We have two special characters:

* A **1-bit character** is represented by `0`.
* A **2-bit character** is represented by either `10` or `11`.

Given a binary array `bits` that ends with `0`, return `True` if the last character must be a one-bit character.

### Example

**Input:**

```text id="a1xqz7"
bits = [1,0,0]
```

**Output:**

```text id="r6n8pk"
True
```

**Explanation:**

The array can be decoded as:

```text id="4q1jmv"
10 | 0
```

The last `0` is a one-bit character.

## 🚀 Approach

We traverse the array from left to right.

* If the current bit is `0`, it represents a one-bit character, so move one position forward.
* If the current bit is `1`, it represents the beginning of a two-bit character, so skip two positions.
* We stop before processing the last bit.
* If the pointer reaches the last index exactly, the last character is a one-bit character.

## 💻 Solution

```python id="k9p2vx"
class Solution:

    def isOneBitCharacter(self, bits: List[int]) -> bool:

        i = 0

        while i < len(bits) - 1:

            if bits[i] == 1:

                i += 2

            else:

                i += 1

        return i == len(bits) - 1
```

## 📊 Complexity Analysis

* **Time Complexity:** `O(n)`
* **Space Complexity:** `O(1)`

The array is traversed from left to right using a single pointer.

## 🧠 Key Concepts

* Array Traversal
* Two Pointers
* Greedy Approach
* Binary Representation

## 🏷️ Difficulty

**Easy**

## 🔗 LeetCode

[1-bit and 2-bit Characters](https://leetcode.com/problems/1-bit-and-2-bit-characters/)
