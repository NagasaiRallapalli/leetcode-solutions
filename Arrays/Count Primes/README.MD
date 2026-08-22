# Count Primes

[![LeetCode](https://img.shields.io/badge/LeetCode-Count%20Primes-orange?style=for-the-badge\&logo=leetcode\&logoColor=white)](https://leetcode.com/problems/count-primes/)

[![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow?style=for-the-badge)](https://leetcode.com/problems/count-primes/)

[![Language](https://img.shields.io/badge/Language-Python-blue?style=for-the-badge\&logo=python\&logoColor=white)](https://www.python.org/)

---

## 📌 Problem Statement

Given an integer `n`, return the number of prime numbers that are strictly less than `n`.

A prime number is a natural number greater than `1` that has no positive divisors other than `1` and itself.

---

## 💡 Example

### Input

```text
n = 10
```

### Output

```text
4
```

### Explanation

The prime numbers less than `10` are:

```text
2, 3, 5, 7
```

Therefore, the answer is:

```text
4
```

---

## 🚀 Approach

This solution uses a separate `isprime()` function to check whether each number is prime.

### Step 1: Handle numbers less than 2

If `n < 2`, there are no prime numbers.

```python
if n < 2:
    return 0
```

### Step 2: Check every number

Loop from `2` to `n - 1`.

```python
for i in range(2, n):
```

For every number, call `isprime(i)`.

### Step 3: Check if a number is prime

A number is prime if it is not divisible by any number from `2` to `√num`.

```python
for i in range(2, int(num**0.5) + 1):
```

If a divisor is found:

```python
if num % i == 0:
    return False
```

Otherwise, the number is prime.

### Step 4: Count the prime numbers

Whenever `isprime(i)` returns `True`, increase the counter.

```python
if self.isprime(i):
    c += 1
```

Finally, return the count.

---

## 💻 Solution

```python
class Solution:

    def isprime(self, num):
        if num < 2:
            return False

        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False

        return True

    def countPrimes(self, n: int) -> int:
        if n < 2:
            return 0

        c = 0

        for i in range(2, n):
            if self.isprime(i):
                c += 1

        return c
```

---

## 📊 Complexity Analysis

| Complexity           | Value      |
| -------------------- | ---------- |
| **Time Complexity**  | **O(n√n)** |
| **Space Complexity** | **O(1)**   |

### ⏱️ Time Complexity

We check every number from `2` to `n - 1`.

For each number, `isprime()` checks divisibility up to its square root.

Therefore, the overall worst-case complexity is approximately:

**O(n√n)**

### 💾 Space Complexity

We only use a few variables such as `c`, `i`, and `num`.

No additional array or data structure is used.

Therefore:

**O(1)** auxiliary space.

---

## 🧠 Key Concepts

* Prime Numbers
* Functions
* Loops
* Square Root Optimization
* Modulo Operator
* Arrays / Number Traversal
* Time Complexity

---

## 🏷️ Difficulty

**Medium** 🟡

---

## 🔗 LeetCode

https://leetcode.com/problems/count-primes/
