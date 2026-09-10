# Intersection of Two Arrays II

![LeetCode](https://img.shields.io/badge/LeetCode-350-orange)
![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## 📌 Problem

Given two integer arrays `nums1` and `nums2`, return an array of their intersection.

Each element in the result must appear as many times as it shows in both arrays.

The result can be returned in any order.

### Example

**Input:**

```text
nums1 = [1,2,2,1]
nums2 = [2,2]
```

**Output:**

```text
[2,2]
```

**Explanation:**

The number `2` appears twice in both arrays, so it appears twice in the result.

---

## 🚀 Approach

This solution uses `nums2` as a changing list to keep track of elements that are already matched.

1. Create an empty list `a` to store the intersection.
2. Traverse every element `i` in `nums1`.
3. Check whether `i` is present in `nums2`.
4. If it is present:

   * Add `i` to the result list.
   * Remove that occurrence from `nums2`.
5. Removing the matched element ensures that duplicate elements are counted correctly.

### Example

```text
nums1 = [1,2,2,1]
nums2 = [2,2]
```

* `1` → not present in `nums2`
* `2` → present → add `2`, remove one `2`
* `2` → present → add `2`, remove the remaining `2`
* `1` → not present

Result:

```text
[2,2]
```

---

## 💻 Solution

```python
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:

        a = []

        for i in nums1:

            if i in nums2:

                a.append(i)

                nums2.remove(i)

        return a
```

---

## 📊 Complexity Analysis

Let `n` be the length of `nums1` and `m` be the length of `nums2`.

| Complexity | Analysis                      |
| ---------- | ----------------------------- |
| Time       | `O(n × m)` in the worst case  |
| Space      | `O(min(n, m))` for the result |

### Why `O(n × m)`?

* `i in nums2` takes `O(m)` in the worst case.
* `nums2.remove(i)` also takes `O(m)` in the worst case.
* These operations are performed while traversing `nums1`.

Therefore, the worst-case time complexity is **O(n × m)**.

---

## 🧠 Key Concepts

* Array traversal
* List membership checking
* Duplicate handling
* `remove()` operation
* Iterative approach

---

## 🏷️ Difficulty

**Easy**

---

## 🔗 LeetCode

[Intersection of Two Arrays II](https://leetcode.com/problems/intersection-of-two-arrays-ii/)
