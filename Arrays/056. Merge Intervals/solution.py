class Solution(object):
    def merge(self, intervals):
        intervals.sort(key=lambda x:x[0])
        a=[]
        for i in intervals:
            if not a or a[-1][1]<i[0]:
                a.append(i)
            else:
                a[-1][1]=max(a[-1][1],i[1])
        return a