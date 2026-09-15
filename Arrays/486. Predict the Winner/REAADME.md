# Predict the Winner

![LeetCode](https://img.shields.io/badge/LeetCode-486-orange)
![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## 📌 Problem

You are given an integer array `nums`. Two players take turns choosing either the first or last number from the array.

Each player adds the chosen number to their score.

Both players play optimally. Return `True` if Player 1 can win or tie with Player 2, otherwise return `False`.

### Example

**Input:**

```text
nums = [1,5,2]
```

**Output:**

```text
False
```

**Explanation:**

Player 1 cannot win when both players play optimally.

---

## 🚀 Approach

This solution uses **recursion** to calculate the maximum score difference the current player can achieve.

The `winner()` function works with the current range from index `i` to `j`.

At every turn, the player has two choices:

1. Pick the **left** element.
2. Pick the **right** element.

For each choice, we subtract the score that the opponent can achieve from the remaining array.

```text
left  = arr[i] - winner(arr, i+1, j)
right = arr[j] - winner(arr, i, j-1)
```

We choose the better option using:

```text
max(left, right)
```

### Base Case

When `i == j`, only one number is left, so the current player takes it:

```text
return arr[i]
```

Finally:

```text
winner(nums, 0, len(nums) - 1) >= 0
```

If the score difference is `0` or positive, Player 1 can win or tie.

---

## 💻 Solution

```python
class Solution:

    def predictTheWinner(self, nums: List[int]) -> bool:

        def winner(arr, i, j):

            if i == j:

                return arr[i]

            left = arr[i] - winner(arr, i+1, j)

            right = arr[j] - winner(arr, i, j - 1)

            return max(left, right)

        return winner(nums, 0, len(nums) - 1) >= 0
```

---

## 📊 Complexity Analysis

Let `n` be the length of `nums`.

| Complexity | Analysis |
| ---------- | -------- |
| Time       | `O(2^n)` |
| Space      | `O(n)`   |

The recursive function explores both the left and right choices at each step, resulting in exponential time.

The recursion depth can reach `n`, so the auxiliary space is `O(n)`.

---

## 🧠 Key Concepts

* Recursion
* Game strategy
* Optimal choice
* Score difference
* Divide and conquer
* Base case

---

## 🏷️ Difficulty

**Medium**

---

## 🔗 LeetCode

[Predict the Winner](https://leetcode.com/problems/predict-the-winner/)
