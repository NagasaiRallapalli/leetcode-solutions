# Single Number III

[![LeetCode](https://img.shields.io/badge/LeetCode-Single%20Number%20III-orange?style=for-the-badge\&logo=leetcode\&logoColor=white)](https://leetcode.com/problems/single-number-iii/)

[![Difficulty](https://img.shields.io/badge/Difficulty-Medium-orange?style=for-the-badge)](https://leetcode.com/problems/single-number-iii/)

[![Language](https://img.shields.io/badge/Language-Python-blue?style=for-the-badge\&logo=python\&logoColor=white)](https://www.python.org/)

---

## 📌 Problem Statement

Given an integer array `nums`, where exactly two elements appear only once and all the other elements appear exactly twice, return the two elements that appear only once.

You may return the answer in any order.

---

## 💡 Example

### Input

```text
nums = [1,2,1,3,2,5]
```

### Output

```text
[3,5]
```

### Explanation

The elements `1` and `2` appear twice.

The elements `3` and `5` appear only once.

Therefore, the two single numbers are:

```text
[3,5]
```

---

## 🚀 Approach

This solution uses **Frequency Counting** with a **Dictionary**.

1. Create an empty dictionary `freq` to store the frequency of each element.

2. Traverse through the array and count how many times each element occurs.

3. Traverse through the dictionary using `items()`.

4. If the frequency of an element is `1`, add it to the result list.

5. Return the result list containing the two single numbers.

---

## 💻 Solution

```python
class Solution:

    def singleNumber(self, nums: List[int]) -> List[int]:

        freq = {}
        s_list = []

        for i in nums:
            if i in freq:
                freq[i] += 1
            else:
                freq[i] = 1

        for key, value in freq.items():
            if value == 1:
                s_list.append(key)

        return s_list
```

---

## 📊 Complexity Analysis

| Complexity           | Value    |
| -------------------- | -------- |
| **Time Complexity**  | **O(n)** |
| **Space Complexity** | **O(n)** |

### ⏱️ Time Complexity

The first loop traverses all `n` elements:

**O(n)**

The second loop traverses the dictionary containing at most `n` distinct elements:

**O(n)**

Therefore, the overall time complexity is:

**O(n)**

### 💾 Space Complexity

The dictionary stores the frequency of the elements.

In the worst case, it can contain `n` distinct elements.

Therefore:

**O(n)**

---

## 🧠 Key Concepts

* Arrays
* Hash Map / Dictionary
* Frequency Counting
* Traversal
* Duplicate Detection
* Single Number

---

## 🏷️ Difficulty

**Medium** 🟡

---

## 🔗 LeetCode

https://leetcode.com/problems/single-number-iii/
