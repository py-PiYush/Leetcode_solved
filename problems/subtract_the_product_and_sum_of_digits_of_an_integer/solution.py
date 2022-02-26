class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        sum, prod = 0, 1
        while n:
            digit = n % 10
            sum += digit
            prod *= digit
            n //= 10
        return prod - sum
        