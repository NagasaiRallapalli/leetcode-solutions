class Solution(object):
    def hasGroupsSizeX(self, deck):
        d={}
        for i in deck:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        def gcd(a,b):
            while b:
                a,b=b,a%b
            return a
        c=0
        for i in d.values():
            c=gcd(c,i)
        return c >= 2