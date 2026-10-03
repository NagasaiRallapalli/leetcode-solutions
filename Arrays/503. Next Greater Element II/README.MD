# Next Greater Element II

![LeetCode](https://img.shields.io/badge/LeetCode-503-orange)
![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## 📌 Problem

Given a circular integer array `nums`, return the next greater number for every element.

The next greater number of an element is the first number greater than it when moving to the right. Since the array is circular, after reaching the last element, we continue from the first element.

If no greater element exists, return `-1`.

### Example

**Input:**

```text
nums = [1,2,1]
```

**Output:**

```text
[2,-1,2]
```

**Explanation:**

* For `1`, the next greater element is `2`.
* For `2`, there is no greater element, so return `-1`.
* For the last `1`, we continue from the beginning and find `2`.

## 🚀 Approach

We use a **Brute Force** approach with a circular array.

* Create `empty_list` with `-1` for every position.
* For every element at index `i`, check the next `n - 1` positions.
* Use modulo `%` to handle the circular nature of the array.
* If a greater element is found, store it in the result and stop searching for that element.
* If no greater element is found, `-1` remains in the result.

The circular index is calculated using:

```python
index = j % len(nums)
```

## 💻 Solution

```python
class Solution:

    def nextGreaterElements(self, nums: List[int]) -> List[int]:

        empty_list = [-1] * len(nums)

        for i in range(len(nums)):

            for j in range(i + 1, i + len(nums)):

                index = j % len(nums)

                if nums[index] > nums[i]:

                    empty_list[i] = nums[index]

                    break

        return empty_list
```

## 📊 Complexity Analysis

* **Time Complexity:** `O(n²)`
* **Space Complexity:** `O(n)`

For every element, we may check up to `n - 1` other elements.

## 🧠 Key Concepts

* Circular Array
* Brute Force
* Nested Loops
* Modulo Operator
* Array Traversal

## 🏷️ Difficulty

**Medium**

## 🔗 LeetCode

[Next Greater Element II](https://leetcode.com/problems/next-greater-element-ii/)