# X of a Kind in a Deck of Cards

![LeetCode](https://img.shields.io/badge/LeetCode-914-orange)
![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## 📌 Problem

Given an integer array `deck`, group the cards so that each group contains exactly `X` cards, where every card in a group has the same integer value.

Return `True` if it is possible to choose `X >= 2` and form such groups. Otherwise, return `False`.

## 💡 Example

**Input:**
```python
deck = [1, 2, 3, 4, 4, 3, 2, 1]
```

**Output:**
```python
True
```

**Explanation:** We can form groups of size `2`: `[1, 1]`, `[2, 2]`, `[3, 3]`, and `[4, 4]`.

## 🚀 Approach

1. Use a dictionary `d` to count the frequency of each card.
2. Define a `gcd(a, b)` function using the Euclidean algorithm to calculate the greatest common divisor.
3. Start with `c = 0` and calculate the GCD of all card frequencies.
4. If the final GCD is at least `2`, equal-sized groups are possible; otherwise, they are not.

## 💻 Solution

```python
class Solution(object):
    def hasGroupsSizeX(self, deck):
        d={}
        for i in deck:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        def gcd(a,b):
            while b:
                a,b=b,a%b
            return a
        c=0
        for i in d.values():
            c=gcd(c,i)
        return c >= 2
```

## 📊 Complexity Analysis

- **Time Complexity:** `O(n + k log n)`, where `n` is the number of cards and `k` is the number of distinct card values.
- **Space Complexity:** `O(k)`, where `k` is the number of distinct card values stored in the dictionary.

## 🧠 Key Concepts

- Hash maps / dictionaries
- Frequency counting
- Greatest Common Divisor (GCD)
- Euclidean algorithm

## 🏷️ Difficulty

Easy

## 🔗 LeetCode

[X of a Kind in a Deck of Cards — LeetCode 914](https://leetcode.com/problems/x-of-a-kind-in-a-deck-of-cards/)