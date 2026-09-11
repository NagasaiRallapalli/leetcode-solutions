# Find All Duplicates in an Array

![LeetCode](https://img.shields.io/badge/LeetCode-442-orange)
![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## 📌 Problem

Given an integer array `nums` of length `n` where all integers are in the range `[1, n]` and each integer appears once or twice, return an array of all the integers that appear twice.

You must solve the problem without using extra space proportional to the input size.

### Example

**Input:**

```text
nums = [4,3,2,7,8,2,3,1]
```

**Output:**

```text
[2,3]
```

**Explanation:**

* `2` appears twice.
* `3` appears twice.
* All other numbers appear only once.

Therefore, the result is `[2,3]`.

---

## 🚀 Approach

This solution uses a **set** to keep track of the elements that have already been seen.

1. Create an empty set `seen`.
2. Create an empty list `result`.
3. Traverse every element `i` in `nums`.
4. If `i` is not present in `seen`, add it to the set.
5. If `i` is already present in `seen`, it is a duplicate, so add it to `result`.
6. Return `result`.

### Example

For:

```text
nums = [4,3,2,7,8,2,3,1]
```

While traversing:

```text
4 → first time
3 → first time
2 → first time
7 → first time
8 → first time
2 → duplicate → add to result
3 → duplicate → add to result
1 → first time
```

Result:

```text
[2,3]
```

---

## 💻 Solution

```python
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:

        seen = set()

        result = []

        for i in nums:

            if i not in seen:

                seen.add(i)

            else:

                result.append(i)

        return result
```

---

## 📊 Complexity Analysis

Let `n` be the number of elements in `nums`.

| Complexity | Analysis |
| ---------- | -------- |
| Time       | `O(n)`   |
| Space      | `O(n)`   |

Each element is checked once, and set operations such as `add()` and checking membership are `O(1)` on average.

---

## 🧠 Key Concepts

* Sets
* Duplicate detection
* Array traversal
* Membership checking
* Iterative approach

---

## 🏷️ Difficulty

**Medium**

---

## 🔗 LeetCode

[Find All Duplicates in an Array](https://leetcode.com/problems/find-all-duplicates-in-an-array/)
