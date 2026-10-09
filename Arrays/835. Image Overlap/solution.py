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