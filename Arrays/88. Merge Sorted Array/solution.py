class Solution(object):
    def merge(self, a, m, b, n):
        c = []
        low = 0
        high = 0
        while low < m and high < n:
            if a[low] < b[high]:
                c.append(a[low])
                low += 1
            else:
                c.append(b[high])
                high += 1
        while low < m:
            c.append(a[low])
            low += 1
        while high < n:
            c.append(b[high])
            high += 1
        for i in range(len(c)):
            a[i] = c[i]