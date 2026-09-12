# Find All Numbers Disappeared in an Array

![LeetCode](https://img.shields.io/badge/LeetCode-448-orange)
![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## 📌 Problem

Given an array `nums` of `n` integers where `nums[i]` is in the range `[1, n]`, return all the integers in the range `[1, n]` that do not appear in `nums`.

### Example

**Input:**

```text
nums = [4,3,2,7,8,2,3,1]
```

**Output:**

```text
[5,6]
```

**Explanation:**

The numbers from `1` to `8` are:

```text
[1,2,3,4,5,6,7,8]
```

The numbers `5` and `6` are missing from the array.

---

## 🚀 Approach

This solution uses a **set** to store all the numbers present in `nums`.

1. Create an empty list `result`.
2. Convert `nums` into a set using `set(nums)` to store unique numbers.
3. Traverse all numbers from `1` to `len(nums)`.
4. Check whether each number is present in `seen`.
5. If it is not present, add it to `result`.
6. Return `result`.

### Example

For:

```text
nums = [4,3,2,7,8,2,3,1]
```

The set becomes:

```text
seen = {1,2,3,4,7,8}
```

Checking numbers from `1` to `8`:

```text
1 → present
2 → present
3 → present
4 → present
5 → missing
6 → missing
7 → present
8 → present
```

Therefore:

```text
result = [5,6]
```

---

## 💻 Solution

```python
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:

        result = []

        seen = set(nums)

        for i in range(1,len(nums)+1):

            if i not in seen:

                result.append(i)

        return result
```

---

## 📊 Complexity Analysis

Let `n` be the length of `nums`.

| Complexity | Analysis |
| ---------- | -------- |
| Time       | `O(n)`   |
| Space      | `O(n)`   |

Creating the set takes `O(n)`, and checking all numbers from `1` to `n` takes `O(n)`.

---

## 🧠 Key Concepts

* Sets
* Duplicate handling
* Missing numbers
* Array traversal
* Membership checking

---

## 🏷️ Difficulty

**Easy**

---

## 🔗 LeetCode

[Find All Numbers Disappeared in an Array](https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/)
