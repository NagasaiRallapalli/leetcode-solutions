# K-diff Pairs in an Array

![LeetCode](https://img.shields.io/badge/LeetCode-532-orange)
![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## 📌 Problem

Given an integer array `nums` and an integer `k`, return the number of **unique k-diff pairs** in the array.

A pair `(i, j)` is called a k-diff pair if:

```text
|nums[i] - nums[j]| == k
```

The pair should be counted only once, even if the same values appear multiple times.

### Example

**Input:**

```text id="6r5f5k"
nums = [3,1,4,1,5]
k = 2
```

**Output:**

```text id="wq1y72"
2
```

**Explanation:**

The unique pairs are:

```text id="fr1h0u"
(1,3)
(3,5)
```

Therefore, the answer is `2`.

---

## 🚀 Approach

This solution uses two sets:

* `seen` → stores the numbers that have already been visited.
* `pairs` → stores unique pairs that satisfy the difference `k`.

### Steps

1. Create an empty set `seen`.
2. Create an empty set `pairs`.
3. Traverse every number `i` in `nums`.
4. Check whether `i - k` is already present in `seen`.

   * If yes, add `(i-k, i)` to `pairs`.
5. Check whether `i + k` is already present in `seen`.

   * If yes, add `(i, i+k)` to `pairs`.
6. Add `i` to `seen`.
7. Return the number of unique pairs using `len(pairs)`.

### Example

For:

```text id="x9p5a1"
nums = [3,1,4,1,5]
k = 2
```

While traversing:

```text id="9z4xkp"
3 → seen = {3}
1 → seen = {1,3}
4 → (3,4) not valid, (4,6) not valid
1 → duplicate value
5 → (3,5) found
```

The valid unique pairs are stored in `pairs`.

---

## 💻 Solution

```python id="6p8k2m"
class Solution:

    def findPairs(self, nums: List[int], k: int) -> int:

        seen = set()

        pairs = set()

        for i in nums:

            if i - k in seen:

                pairs.add((i - k, i))

            if i + k in seen:

                pairs.add((i, i + k))

            seen.add(i)

        return len(pairs)
```

---

## 📊 Complexity Analysis

Let `n` be the length of `nums`.

| Complexity | Analysis          |
| ---------- | ----------------- |
| Time       | `O(n)` on average |
| Space      | `O(n)`            |

Each element is processed once, and set operations such as lookup and insertion take `O(1)` on average.

---

## 🧠 Key Concepts

* Sets
* Hashing
* Unique pairs
* Duplicate handling
* Set membership checking
* Tuple storage

---

## 🏷️ Difficulty

**Medium**

---

## 🔗 LeetCode

[K-diff Pairs in an Array](https://leetcode.com/problems/k-diff-pairs-in-an-array/)
