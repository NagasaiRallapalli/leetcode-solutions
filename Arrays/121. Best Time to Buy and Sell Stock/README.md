# Best Time to Buy and Sell Stock

[![LeetCode](https://img.shields.io/badge/LeetCode-Best%20Time%20to%20Buy%20and%20Sell%20Stock-orange?style=for-the-badge&logo=leetcode&logoColor=white)](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/)
[![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green?style=for-the-badge)]()
[![Language](https://img.shields.io/badge/Language-Python-blue?style=for-the-badge&logo=python&logoColor=white)]()

---

## 📌 Problem Statement

You are given an array `prices` where `prices[i]` represents the price of a stock on the `ith` day.

Choose one day to buy the stock and a different day in the future to sell it.

Return the maximum profit you can achieve. If no profit is possible, return `0`.

---

## 💡 Example

### Input

```text
prices = [7,1,5,3,6,4]
```

### Output

```text
5
```

### Explanation

Buy the stock at price `1` and sell it at price `6`.

```text
Profit = 6 - 1 = 5
```

---

## 🚀 Approach

This solution uses a **Two Pointer / Greedy** approach.

1. Use `l` as the buying day.
2. Use `r` as the selling day.
3. If `prices[r] > prices[l]`, calculate the current profit.
4. Update the maximum profit.
5. If `prices[r] <= prices[l]`, move the buying pointer to `r`.
6. Continue until the end of the array.

---

## 💻 Solution

```python
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        maxp = 0

        while r < len(prices):
            if prices[l] < prices[r]:
                p = prices[r] - prices[l]
                maxp = max(maxp, p)
            else:
                l = r

            r += 1

        return maxp
```

---

## 📊 Complexity Analysis

| Complexity | Value |
|------------|-------|
| **Time Complexity** | **O(n)** |
| **Space Complexity** | **O(1)** |

### ⏱️ Time Complexity

The array is traversed only once.

**O(n)**

### 💾 Space Complexity

Only a few variables are used.

**O(1)**

---

## 🧠 Key Concepts

- Arrays
- Two Pointers
- Greedy Algorithm
- Maximum Profit
- Array Traversal

---

## 🏷️ Difficulty

**Easy** 🟢

---

## 🔗 LeetCode

https://leetcode.com/problems/best-time-to-buy-and-sell-stock/