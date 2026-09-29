# Maximum Product of Word Lengths

![LeetCode](https://img.shields.io/badge/LeetCode-318-orange)
![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## 📌 Problem

Given a string array `words`, find the maximum value of `length(word[i]) * length(word[j])` where the two words do not share any common letters.

If no such pair exists, return `0`.

### Example

**Input:**

```text id="2qv1c8"
words = ["abcw","baz","foo","bar","xtfn","abcdef"]
```

**Output:**

```text id="a8l0wz"
16
```

**Explanation:**

The words `"abcw"` and `"xtfn"` have no common characters.

Their lengths are `4` and `4`, so:

```text
4 × 4 = 16
```

## 🚀 Approach

We use **Sets** to check whether two words have any common characters.

* Create a set for every word and store it in `seen`.
* Compare every pair of words using two loops.
* Use `intersection()` to check for common characters.
* If the intersection is empty, the two words have no common characters.
* Calculate the product of their lengths and keep the maximum value.

## 💻 Solution

```python id="j4x2rm"
class Solution:

    def maxProduct(self, words: list[str]) -> int:

        prod = 0

        seen = []

        for word in words:

            seen.append(set(word))

        for i in range(len(words)):

            for j in range(i + 1, len(words)):

                if not seen[i].intersection(seen[j]):

                    prod = max(prod, len(words[i]) * len(words[j]))

        return prod
```

## 📊 Complexity Analysis

* **Time Complexity:** `O(n² × k)`
* **Space Complexity:** `O(n × k)`

Where `n` is the number of words and `k` is the average length of a word.

The two nested loops compare every pair of words, while set intersection checks their characters.

## 🧠 Key Concepts

* Hash Set
* Set Intersection
* String
* Brute Force
* Nested Loops

## 🏷️ Difficulty

**Medium**

## 🔗 LeetCode

[Maximum Product of Word Lengths](https://leetcode.com/problems/maximum-product-of-word-lengths/)
