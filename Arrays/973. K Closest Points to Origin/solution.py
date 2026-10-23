class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        arr = []
        for i in points:
            x = i[0]
            y = i[1]
            d = x * x + y * y
            arr.append([d, i])
        arr.sort()
        ans = []
        for i in range(k):
            ans.append(arr[i][1])
        return ans