class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        lst=map(int,str(n))
        sum=0
        product=1
        for i in lst:
            sum+=i
            product*=i
        return product-sum
        