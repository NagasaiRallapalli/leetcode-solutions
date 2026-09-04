# Contains Duplicate II

[![LeetCode](https://img.shields.io/badge/LeetCode-Contains%20Duplicate%20II-orange?style=for-the-badge\&logo=leetcode\&logoColor=white)](https://leetcode.com/problems/contains-duplicate-ii/)

[![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green?style=for-the-badge)](https://leetcode.com/problems/contains-duplicate-ii/)

[![Language](https://img.shields.io/badge/Language-Python-blue?style=for-the-badge\&logo=python\&logoColor=white)]()

---

# 📌 Problem Statement

Given an integer array `nums` and an integer `k`, return `true` if there are two distinct indices `i` and `j` such that:

* `nums[i] == nums[j]`
* `abs(i - j) <= k`

Otherwise, return `false`.

---

# 💡 Example

### Input

```text
nums = [1,2,3,1]
k = 3
```

### Output

```text
true
```

### Explanation

The value `1` appears at indices `0` and `3`.

The difference between their indices is:

```text
3 - 0 = 3
```

Since `3 <= k`, the answer is `true`.

---

# 🚀 Approach

This solution uses a **Hash Map (Dictionary)** to store the **last index** where each number appeared.

1. Create an empty dictionary `freq`.
2. Traverse the array using index `i`.
3. If `nums[i]` already exists in the dictionary:

   * Calculate the distance between the current index and its previous index.
   * If the distance is `<= k`, return `True`.
4. Update the dictionary with the current index.
5. If no nearby duplicate is found, return `False`.

This allows us to check previous occurrences in **O(1)** average time.

---

# 💻 Solution

```python
class Solution:

    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:

        freq = {}

        for i in range(len(nums)):

            if nums[i] in freq and i - freq[nums[i]] <= k:
                return True

            freq[nums[i]] = i

        return False
```

---

# 📊 Complexity Analysis

| Complexity           | Value    |
| -------------------- | -------- |
| **Time Complexity**  | **O(n)** |
| **Space Complexity** | **O(n)** |

---

# 🧠 Key Concepts

* Arrays
* Hash Map
* Dictionary
* Duplicate Detection
* Index Tracking

---

# 🏷️ Difficulty

**Easy** 🟢

---

# 🔗 LeetCode

https://leetcode.com/problems/contains-duplicate-ii/
