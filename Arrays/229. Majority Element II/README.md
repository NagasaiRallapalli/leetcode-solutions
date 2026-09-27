# Majority Element II

![LeetCode](https://img.shields.io/badge/LeetCode-229-orange)
![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## 📌 Problem

Given an integer array `nums` of size `n`, return all elements that appear more than `n / 3` times.

### Example

**Input:**

```text
nums = [3,2,3]
```

**Output:**

```text
[3]
```

**Explanation:**

The element `3` appears 2 times, which is more than `3 / 3 = 1`.

## 🚀 Approach

We use a **Hash Map / Dictionary** to count the frequency of every element.

* Create a dictionary `freq` to store the frequency of each number.
* Traverse the array and update the frequency of every element.
* Traverse the dictionary and check if the frequency is greater than `len(nums) // 3`.
* Add such elements to the result list.

## 💻 Solution

```python id="t3d5rz"
class Solution:

    def majorityElement(self, nums: List[int]) -> List[int]:

        freq = {}

        for i in nums:

            if i not in freq:

                freq[i] = 1

            else:

                freq[i] += 1

        ans = []

        for key, val in freq.items():

            if val > len(nums) // 3:

                ans.append(key)

        return ans
```

## 📊 Complexity Analysis

* **Time Complexity:** `O(n)`
* **Space Complexity:** `O(n)`

The array is traversed to count frequencies, and the frequency dictionary is traversed to find the required elements.

## 🧠 Key Concepts

* Hash Map
* Frequency Counting
* Array
* Dictionary

## 🏷️ Difficulty

**Medium**

## 🔗 LeetCode

[Majority Element II](https://leetcode.com/problems/majority-element-ii/)
