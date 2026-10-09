# Image Overlap

![LeetCode](https://img.shields.io/badge/LeetCode-835-orange)
![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## 📌 Problem

You are given two binary square matrices, `img1` and `img2`. Return the largest possible number of overlapping `1`s when one image is translated over the other.

### Example

**Input:**

```text
img1 = [[1,1,0],
        [0,1,0],
        [0,1,0]]

img2 = [[0,0,0],
        [0,1,1],
        [0,0,1]]
```

**Output:**

```text
3
```

**Explanation:**

By shifting one image horizontally and vertically, three `1`s can overlap.

## 🚀 Approach

We use a **Coordinate Difference + Hash Map** approach.

* Store the coordinates of all `1`s in `img1` in list `a`.
* Store the coordinates of all `1`s in `img2` in list `b`.
* Compare every coordinate in `a` with every coordinate in `b`.
* Calculate the row and column differences for each pair.
* Store the frequency of each `(row, col)` shift in the dictionary `count`.
* The most frequent shift gives the maximum overlap.
* If no coordinate pairs exist, return `0`.

## 💻 Solution

```python
class Solution:
    def largestOverlap(self, img1: list[list[int]], img2: list[list[int]]) -> int:
        n = len(img1)
        a = []
        for i in range(n):
            for j in range(len(img1[i])):
                if img1[i][j] == 1:
                    a.append((i, j))

        m = len(img2)
        b = []
        for i in range(m):
            for j in range(len(img2[i])):
                if img2[i][j] == 1:
                    b.append((i, j))
        
        count = {}
        for i in a:
            for j in b:
                row = j[0] - i[0]
                col = j[1] - i[1]
                if (row, col) in count:
                    count[(row, col)] += 1
                else:
                    count[(row, col)] = 1
        if len(count) == 0:
            return 0
        return max(count.values())
```

## 📊 Complexity Analysis

Let `n` be the image dimension, `p` the number of `1`s in `img1`, and `q` the number of `1`s in `img2`.

* **Time Complexity:** `O(n² + p × q)`
* **Space Complexity:** `O(p × q)` in the worst case.

The coordinate lists require space proportional to the number of `1`s, and the dictionary stores the possible coordinate shifts.

## 🧠 Key Concepts

* Matrix Traversal
* Coordinates
* Hash Map
* Frequency Counting
* Geometry

## 🏷️ Difficulty

**Medium**

## 🔗 LeetCode

[Image Overlap](https://leetcode.com/problems/image-overlap/)
