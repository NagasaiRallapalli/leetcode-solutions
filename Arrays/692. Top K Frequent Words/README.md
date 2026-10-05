# Top K Frequent Words

![LeetCode](https://img.shields.io/badge/LeetCode-692-orange)
![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## 📌 Problem

Given an array of strings `words` and an integer `k`, return the `k` most frequent strings.

The words with higher frequency should come first. If two words have the same frequency, they should be ordered alphabetically.

### Example

**Input:**

```text id="k4f7de"
words = ["i","love","leetcode","i","love","coding"]
k = 2
```

**Output:**

```text id="d7u9k3"
["i","love"]
```

**Explanation:**

* `"i"` appears 2 times.
* `"love"` appears 2 times.
* `"leetcode"` and `"coding"` appear once.
* Since `"i"` and `"love"` have the same frequency, they are ordered alphabetically.

## 🚀 Approach

We use a **Hash Map / Dictionary** to count the frequency of every word.

1. Store the frequency of each word in `freq`.
2. Create a list `a` containing all unique words.
3. Sort the words initially in alphabetical order.
4. Use nested loops to arrange the words:

   * Higher frequency comes first.
   * If frequencies are equal, alphabetical order is used.
5. Take the first `k` words and store them in `ans`.

## 💻 Solution

```python
class Solution:
    def topKFrequent(self, words: list[str], k: int) -> list[str]:
        freq = {}
        for i in words:
            if i not in freq:
                freq[i] = 1
            else:
                freq[i] += 1

        a = list(freq.keys())
        a.sort()

        for i in range(len(a)):
            for j in range(i + 1, len(a)):
                if freq[a[i]] < freq[a[j]]:
                    a[i], a[j] = a[j], a[i]
                elif freq[a[i]] == freq[a[j]] and a[i] > a[j]:
                    a[i], a[j] = a[j], a[i]
                    
        ans = []
        for i in range(k):
            ans.append(a[i])
        return ans
```

## 📊 Complexity Analysis

* **Time Complexity:** `O(n + m²)`
* **Space Complexity:** `O(m)`

Where `n` is the number of words and `m` is the number of unique words.

The frequency counting takes `O(n)` time, and the nested loops take `O(m²)` time.

## 🧠 Key Concepts

* Hash Map
* Frequency Counting
* String Sorting
* Nested Loops
* Lexicographical Order

## 🏷️ Difficulty

**Medium**

## 🔗 LeetCode

[Top K Frequent Words](https://leetcode.com/problems/top-k-frequent-words/)
