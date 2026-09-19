# Distribute Candies

![LeetCode](https://img.shields.io/badge/LeetCode-575-orange)
![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## 📌 Problem

Alice has `n` candies, where `n` is even. Each candy has a type represented by an integer in `candyType`.

Alice wants to eat exactly `n / 2` candies.

Return the maximum number of different types of candies she can eat.

### Example

**Input:**

```text id="m5v2sq"
candyType = [1,1,2,2,3,3]
```

**Output:**

```text id="q7x0w1"
3
```

**Explanation:**

There are 3 different candy types:

```text id="7h9q4x"
1, 2, 3
```

Alice can eat `n / 2 = 3` candies, so she can eat all 3 different types.

---

## 🚀 Approach

The answer depends on two values:

1. **Number of unique candy types**

   ```text
   len(set(candyType))
   ```

2. **Maximum number of candies Alice can eat**

   ```text
   len(candyType) // 2
   ```

Alice cannot eat more than half of the candies, and she cannot eat more different types than the number of unique types available.

Therefore, we take the minimum of these two values:

```text
min(len(set(candyType)), len(candyType)//2)
```

### Example

For:

```text id="g7y4nb"
candyType = [1,1,2,2,3,3]
```

Unique types:

```text
3
```

Candies Alice can eat:

```text
6 // 2 = 3
```

Therefore:

```text
min(3, 3) = 3
```

---

## 💻 Solution

```python id="x6v9pk"
class Solution:
    def distributeCandies(self, candyType: list[int]) -> int:
        return min(len(set(candyType)), len(candyType)//2)
```

---

## 📊 Complexity Analysis

Let `n` be the number of candies.

| Complexity | Analysis |
| ---------- | -------- |
| Time       | `O(n)`   |
| Space      | `O(n)`   |

Creating the set requires `O(n)` time and `O(n)` additional space in the worst case.

---

## 🧠 Key Concepts

* Sets
* Removing duplicates
* `len()`
* `min()`
* Integer division
* Simple mathematical observation

---

## 🏷️ Difficulty

**Easy**

---

## 🔗 LeetCode

[Distribute Candies](https://leetcode.com/problems/distribute-candies/)
