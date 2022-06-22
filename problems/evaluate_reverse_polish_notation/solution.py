class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        evaluate = {
            '+': lambda a,b : a+b,
            '-': lambda a,b : a-b,
            '*': lambda a,b : a*b,
            '/': lambda a,b : int(a/b)
        }
        stack = []
        for c in tokens:
            if c in evaluate:
                val2, val1 = stack.pop(), stack.pop()
                stack.append(evaluate[c](val1,val2))
            else:
                stack.append(int(c))
        return stack.pop()
        
    
        '''-------------------------------------------'''
        operators = {'+', '-', '*', '/'}
        stack = []
        for c in tokens:
            # print(stack)
            if c in operators:
                val2, val1 = stack.pop(), stack.pop()
                if c == '+':
                    stack.append(val1 + val2)
                elif c == '-':
                    stack.append(val1 - val2)
                elif c == '*':
                    stack.append(val1*val2)
                else:
                    stack.append(int(val1/val2))
            else:
                stack.append(int(c))
        return stack[0]