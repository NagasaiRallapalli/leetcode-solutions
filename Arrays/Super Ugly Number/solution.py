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