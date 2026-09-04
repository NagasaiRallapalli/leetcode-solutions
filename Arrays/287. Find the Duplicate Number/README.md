# Find the Duplicate Number

[![LeetCode](https://img.shields.io/badge/LeetCode-Find%20the%20Duplicate%20Number-orange?style=for-the-badge\&logo=leetcode\&logoColor=white)](https://leetcode.com/problems/find-the-duplicate-number/)

[![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow?style=for-the-badge)](https://leetcode.com/problems/find-the-duplicate-number/)

[![Language](https://img.shields.io/badge/Language-Python-blue?style=for-the-badge\&logo=python\&logoColor=white)](https://www.python.org/)

---

## 📌 Problem Statement

Given an array of integers `nums` containing `n + 1` integers where each integer is in the range `[1, n]`, return the **only duplicate number** in the array.

There is only one repeated number, but it may be repeated more than once.

---

## 💡 Example

### Input

```text
nums = [1, 3, 4, 2, 2]
```

### Output

```text
2
```

### Explanation

The number `2` appears more than once in the array.

Therefore, the duplicate number is:

```text
2
```

---

## 🚀 Approach

This solution uses a **set** to keep track of the numbers that have already been seen.

### Step 1: Create a Set

Create an empty set called `seen`.

```python
seen = set()
```

The set stores the numbers that have already appeared in the array.

### Step 2: Traverse the Array

Loop through every element in `nums`.

```python
for i in nums:
```

### Step 3: Check for Duplicate

If the current number is already present in `seen`, it means that the number has appeared before and is therefore the duplicate.

```python
if i in seen:
    return i
```

### Step 4: Add the Number to the Set

If the number has not appeared before, add it to the set.

```python
seen.add(i)
```

When a duplicate number is found, return it immediately.

---

## 💻 Solution

```python
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        seen = set()

        for i in nums:
            if i in seen:
                return i
            seen.add(i)
```

---

## 📊 Complexity Analysis

| Complexity           | Value    |
| -------------------- | -------- |
| **Time Complexity**  | **O(n)** |
| **Space Complexity** | **O(n)** |

### ⏱️ Time Complexity

We traverse the array only once.

Checking whether an element exists in a set takes **O(1)** average time.

Therefore, the overall time complexity is:

**O(n)**

### 💾 Space Complexity

In the worst case, the set can store up to `n` different elements.

Therefore, the auxiliary space complexity is:

**O(n)**

---

## 🧠 Key Concepts

* Sets
* Duplicate Detection
* Array Traversal
* Hashing
* Membership Checking
* Time Complexity
* Space Complexity

---

## 🏷️ Difficulty

**Medium** 🟡

---

## 🔗 LeetCode

https://leetcode.com/problems/find-the-duplicate-number/
