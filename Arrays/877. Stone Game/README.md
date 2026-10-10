# Stone Game

![LeetCode](https://img.shields.io/badge/LeetCode-877-orange)
![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## 📌 Problem

Alice and Bob play a game with an even number of piles of stones. Each pile contains a positive number of stones.

They take turns choosing either the first or last pile, and Alice goes first. The game ends when all piles are taken. The player with the most stones wins.

Given the array `piles`, return `True` if Alice wins, assuming both players play optimally.

### Example

**Input:**

```text
piles = [5,3,4,5]
```

**Output:**

```text
True
```

**Explanation:**

Alice can guarantee a win when both players play optimally.

## 🚀 Approach

The solution directly returns `True`.

For the original problem, the number of piles is even and every pile contains a positive number of stones. Under these conditions, Alice can always guarantee a win by playing optimally.

## 💻 Solution

```python
class Solution:

    def stoneGame(self, piles: List[int]) -> bool:

        return True
```

## 📊 Complexity Analysis

* **Time Complexity:** `O(1)`
* **Space Complexity:** `O(1)`

The function returns a constant value without processing the input.

## 🧠 Key Concepts

* Game Theory
* Optimal Strategy
* Mathematical Observation

## 🏷️ Difficulty

**Medium**

## 🔗 LeetCode

[Stone Game](https://leetcode.com/problems/stone-game/)
