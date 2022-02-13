class Solution:
    def countOperations(self, num1: int, num2: int) -> int:
        oper=0
        while True:
            if num1==0 or num2==0:
                break
            oper+=1
            if num1>=num2:
                num1-=num2
            else:
                num2-=num1
        return oper