# Longest Substring Without Repeating Characters

![LeetCode](https://img.shields.io/badge/LeetCode-3-orange)
![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## 📌 Problem

Given a string `s`, find the length of the longest substring without repeating characters.

### Example

**Input:**

```text
s = "abcabcbb"
```

**Output:**

```text
3
```

**Explanation:**

The longest substring without repeating characters is `"abc"`, which has a length of `3`.

## 🚀 Approach

We use a **Sliding Window** with a `set`.

* `seen` stores the characters currently present in the window.
* `last` represents the starting index of the current window.
* `i` moves through the string.
* If `s[i]` is already in `seen`, we remove characters from the left until the duplicate is removed.
* Then we add the current character to `seen`.
* Update the maximum length using:

```python
i - last + 1
```

## 💻 Solution

```python
class Solution:

    def lengthOfLongestSubstring(self, s: str) -> int:

        seen = set()

        last = 0

        ans = 0

        for i in range(len(s)):

            while s[i] in seen:

                seen.remove(s[last])

                last += 1

            seen.add(s[i])

            ans = max(ans, i - last + 1)

        return ans
```

## 📊 Complexity Analysis

* **Time Complexity:** `O(n)`
* **Space Complexity:** `O(n)`

Each character is added to and removed from the set at most once, so the overall time complexity is `O(n)`.

## 🧠 Key Concepts

* Sliding Window
* Set
* Two Pointers
* String Traversal

## 🏷️ Difficulty

**Medium**

## 🔗 LeetCode

[Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/)
