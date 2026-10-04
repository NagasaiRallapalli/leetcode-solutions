# Set Mismatch

![LeetCode](https://img.shields.io/badge/LeetCode-645-orange)
![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## 📌 Problem

You are given an integer array `nums` containing numbers from `1` to `n`. Due to an error, one number is duplicated and another number is missing.

Return an array containing:

* The duplicated number.
* The missing number.

### Example

**Input:**

```text
nums = [1,2,2,4]
```

**Output:**

```text
[2,3]
```

**Explanation:**

* `2` appears twice, so it is the duplicated number.
* `3` is missing from the array.

## 🚀 Approach

We use a **Hash Map / Dictionary** to count the frequency of each number.

* Create a dictionary named `freq`.
* Traverse the array and count the occurrences of each number.
* Find the number whose frequency is `2` and add it to `ans`.
* Traverse the range from `1` to `n`.
* If a number is not present in `freq`, add it to `ans` as the missing number.
* Return `ans`.

## 💻 Solution

```python
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        a = set(nums)
        freq = {}
        for i in nums:
            if i not in freq:
                freq[i] = 1
            else:
                freq[i] += 1

        ans = []
        for key, val in freq.items():
            if val == 2:
                ans.append(key)
        for i in range(1, len(nums) + 1):
            if i not in freq:
                ans.append(i)
        return ans
```

## 📊 Complexity Analysis

* **Time Complexity:** `O(n)`
* **Space Complexity:** `O(n)`

The frequency dictionary stores the occurrences of the elements, and we traverse the expected range to find the missing number.

## 🧠 Key Concepts

* Hash Map
* Frequency Counting
* Set
* Array Traversal

## 🏷️ Difficulty

**Easy**

## 🔗 LeetCode

[Set Mismatch](https://leetcode.com/problems/set-mismatch/)
