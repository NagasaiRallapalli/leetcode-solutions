# Contains Duplicate

[![LeetCode](https://img.shields.io/badge/LeetCode-Contains%20Duplicate-orange?style=for-the-badge\&logo=leetcode\&logoColor=white)](https://leetcode.com/problems/contains-duplicate/)

[![Difficulty](https://img.shields.io/badge/Difficulty-Easy-brightgreen?style=for-the-badge)](https://leetcode.com/problems/contains-duplicate/)

[![Language](https://img.shields.io/badge/Language-Python-blue?style=for-the-badge\&logo=python\&logoColor=white)](https://www.python.org/)

---

## 📌 Problem Statement

Given an integer array `nums`, return `True` if any value appears at least twice in the array, and return `False` if every element is distinct.

---

## 💡 Example

### Input

```text
nums = [1, 2, 3, 1]
```

### Output

```text
True
```

### Explanation

The number `1` appears twice in the array.

Therefore, the array contains a duplicate.

---

## 🚀 Approach

This solution uses **sorting** to detect duplicate elements.

### Step 1: Sort the array

First, sort the array so that duplicate elements become adjacent.

```python
nums.sort()
```

For example:

```text
Before: [1, 2, 3, 1]

After:  [1, 1, 2, 3]
```

### Step 2: Compare adjacent elements

After sorting, check every pair of adjacent elements.

```python
if nums[i + 1] == nums[i]:
```

If two adjacent elements are equal, a duplicate exists.

Therefore, return:

```python
return True
```

### Step 3: No duplicate found

If the loop finishes without finding equal adjacent elements, return:

```python
return False
```

---

## 💻 Solution

```python
class Solution(object):

    def containsDuplicate(self, nums):

        nums.sort()

        for i in range(len(nums) - 1):

            if nums[i + 1] == nums[i]:

                return True

        else:

            return False
```

---

## 📊 Complexity Analysis

| Complexity           | Value                    |
| -------------------- | ------------------------ |
| **Time Complexity**  | **O(N log N)**           |
| **Space Complexity** | **O(1)** auxiliary space |

### ⏱️ Time Complexity

The `sort()` operation takes:

**O(N log N)**

The loop takes:

**O(N)**

Therefore, the overall complexity is:

**O(N log N)**

### 💾 Space Complexity

No additional data structure is used.

Therefore, the auxiliary space complexity is:

**O(1)**

> Note: Python's `sort()` may use some internal temporary memory.

---

## 🧠 Key Concepts

* Arrays
* Sorting
* Duplicate Detection
* Adjacent Element Comparison
* Loops
* Time Complexity
* Space Complexity

---

## 🏷️ Difficulty

**Easy** 🟢

---

## 🔗 LeetCode

[Contains Duplicate](https://leetcode.com/problems/contains-duplicate/)
