# Nth Super Ugly Number

[![LeetCode](https://img.shields.io/badge/LeetCode-Nth%20Super%20Ugly%20Number-orange)](https://leetcode.com/problems/super-ugly-number/)

[![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)](https://leetcode.com/problems/super-ugly-number/)

## 📌 Problem

A **Super Ugly Number** is a positive integer whose prime factors are in the given array `primes`.

Given an integer `n` and an array of prime numbers `primes`, return the `n`th super ugly number.

---

## 💡 Example

### Input

```text
n = 12
primes = [2,7,13,19]
```

### Output

```text
32
```

### Explanation

The first 12 super ugly numbers are:

```text
1, 2, 4, 7, 8, 13, 14, 16, 19, 26, 28, 32
```

Therefore, the 12th super ugly number is **32**.

---

## 🚀 Approach

We use **Dynamic Programming + Multiple Pointers**.

1. Start the array with `1`, because `1` is considered the first super ugly number.

2. Create a pointer `p` for every prime in `primes`.

3. Each pointer tells us which previously generated number should be multiplied by its corresponding prime.

4. Find the minimum possible next super ugly number:

   `a[p[j]] * primes[j]`

5. Add this minimum value to the array.

6. If multiple primes produce the same minimum value, move all their pointers forward.

7. Continue until we generate `n` super ugly numbers.

8. Return the last element.

The pointers help us generate the numbers in increasing order without generating unnecessary values.

---

## 💻 Solution

```python
class Solution:

    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:

        a = []

        a.append(1)

        p = [0] * len(primes)

        while len(a) < n:

            aa = min(a[p[j]] * primes[j] for j in range(len(primes)))

            a.append(aa)

            for j in range(len(primes)):

                if a[p[j]] * primes[j] == aa:
                    p[j] += 1

        return a[-1]
```

---

## 📊 Complexity Analysis

Let `k = len(primes)`.

| Complexity       | Value        |
| ---------------- | ------------ |
| Time Complexity  | **O(n × k)** |
| Space Complexity | **O(n + k)** |

### Time Complexity

**O(n × k)** because we generate `n` super ugly numbers and for every number we check all `k` primes.

### Space Complexity

**O(n + k)** because we store the generated super ugly numbers in `a` and maintain `k` pointers in `p`.

---

## 🧠 Key Concepts

* Arrays
* Dynamic Programming
* Multiple Pointers
* Prime Numbers
* Sequence Generation

---

## 🏷️ Difficulty

**Medium**

---

## 🔗 LeetCode

[View Problem on LeetCode](https://leetcode.com/problems/super-ugly-number/)
