class Solution:
    def isprime(self,num):
        if num<2:
            return False
        for i in range(2,int(num**0.5)+1):
            if num%i==0:
                return False
        return True
    def countPrimes(self, n: int) -> int:
        if n<2:
            return 0
        c=0
        for i in range(2,n):
            if self.isprime(i):
                c+=1
        return c