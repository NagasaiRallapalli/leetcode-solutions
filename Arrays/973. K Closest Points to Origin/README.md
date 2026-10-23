# K Closest Points to Origin

![LeetCode](https://img.shields.io/badge/LeetCode-973-orange)
![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## 📌 Problem

Given an array `points`, where `points[i] = [x, y]` represents a point on the 2D plane, and an integer `k`, return the `k` points closest to the origin `(0, 0)`.

The distance between a point `(x, y)` and the origin is calculated using the squared Euclidean distance:

`d = x² + y²`

The order of the returned points does not matter.

## 💡 Example

**Input:**
```python
points = [[1, 3], [-2, 2]]
k = 1
```

**Output:**
```python
[[-2, 2]]
```

**Explanation:** The squared distance of `[1, 3]` is `10`, while the squared distance of `[-2, 2]` is `8`. Therefore, `[-2, 2]` is closer to the origin.

## 🚀 Approach

1. Create an empty list `arr`.
2. Iterate through each point and extract its `x` and `y` coordinates.
3. Calculate the squared distance using `x*x + y*y`.
4. Store each point along with its squared distance in `arr`.
5. Sort `arr` in ascending order based on distance.
6. Select the first `k` points and store them in `ans`.
7. Return `ans`.

## 💻 Solution

```python
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        arr=[]
        for i in points:
            x=i[0]
            y=i[1]
            d=x*x+y*y
            arr.append([d,i])
        arr.sort()
        ans=[]
        for i in range(k):
            ans.append(arr[i][1])
        return ans
```

## 📊 Complexity Analysis

Let `n` be the number of points.

- **Time Complexity:** `O(n log n)` — Calculating distances takes `O(n)`, and sorting takes `O(n log n)`.
- **Space Complexity:** `O(n)` — The auxiliary list `arr` stores the distances and points, and `ans` stores the `k` closest points.

## 🧠 Key Concepts

- Arrays and lists
- Euclidean distance
- Sorting
- Basic geometry

## 🏷️ Difficulty

Medium

## 🔗 LeetCode

[K Closest Points to Origin — LeetCode 973](https://leetcode.com/problems/k-closest-points-to-origin/)