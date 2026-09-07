# Top K Frequent Elements

![LeetCode](https://img.shields.io/badge/LeetCode-347-orange)
![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## 📌 Problem

Given an integer array `nums` and an integer `k`, return the `k` most frequent elements.

You may return the answer in any order.

### Example

**Input:**

```text
nums = [1,1,1,2,2,3]
k = 2
```

**Output:**

```text
[1,2]
```

**Explanation:**

* `1` appears 3 times.
* `2` appears 2 times.
* `3` appears 1 time.

The 2 most frequent elements are `1` and `2`.

---

## 🚀 Approach

The solution uses the following steps:

1. Create a set from `nums` to get only unique elements.
2. Store the frequency of each unique element in a separate list.
3. Find the maximum frequency using `max()`.
4. Find the index of that maximum frequency.
5. Add the corresponding element to the answer.
6. Remove that element and its frequency from the lists.
7. Repeat until `k` elements are selected.

### Example

For:

```text
nums = [1,1,1,2,2,3]
k = 2
```

Unique elements:

```text
c = [1,2,3]
```

Frequencies:

```text
b = [3,2,1]
```

First maximum:

```text
3 → element 1
```

Second maximum:

```text
2 → element 2
```

Result:

```text
[1,2]
```

---

## 💻 Solution

```python
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        a = []
        c = list(set(nums))
        b = []

        for i in c:
            b.append(nums.count(i))

        while k > 0:
            m = max(b)
            x = b.index(m)
            a.append(c[x])
            c.pop(x)
            b.pop(x)
            k -= 1

        return a
```

---

## 📊 Complexity Analysis

Let `n` be the number of elements in `nums`.

| Complexity | Analysis                  |
| ---------- | ------------------------- |
| Time       | `O(n²)` in the worst case |
| Space      | `O(n)`                    |

### Why `O(n²)`?

* `nums.count(i)` takes `O(n)` for each unique element.
* `max(b)` and `index()` are also linear operations.
* Therefore, the overall worst-case time complexity is `O(n²)`.

---

## 🧠 Key Concepts

* Sets
* Frequency counting
* Lists
* `max()`
* `index()`
* List `pop()`
* Iterative approach

---

## 🏷️ Difficulty

**Medium**

---

## 🔗 LeetCode

[Top K Frequent Elements](https://leetcode.com/problems/top-k-frequent-elements/)
