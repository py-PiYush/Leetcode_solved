class Solution:
    def calculate(self, s: str) -> int:
        if not len(s): return 0
        stack=[]
        curNum=0
        operators={'+','-','*','/'}
        oper='+'
        for i in range(len(s)):
            c=s[i]
            if c.isdigit():
                curNum=curNum*10 + int(c)
            if c in operators or i==len(s)-1:
                if oper=='+':
                    stack.append(curNum)
                elif oper=='-':
                    stack.append(-curNum)
                elif oper=='*':
                    stack[-1]*=curNum
                elif oper=='/':
                    stack[-1]=int(stack[-1]/curNum)
                curNum=0
                oper=c
        return sum(stack)
            
            