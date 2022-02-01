class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        sol = [''] * n
        three, five = 3, 5
        
        for i in range(1, n+1):
            if i == three == five:
                sol[i-1] = 'FizzBuzz'
                three += 3
                five += 5
            elif i == five:
                sol[i-1] = 'Buzz'
                five += 5
            elif i == three:
                sol[i-1] = 'Fizz'
                three += 3
            else:
                sol[i-1] = str(i)

        return sol

        
        
        
        '''-----------------'''
        return [str(i)*( i%3!=0 and i%5!=0) + 'Fizz'*(i%3==0) + 'Buzz'*(i%5==0) for i in range(1, n+1)]
        
        
        
        '''---------------------'''
        answer=[]
        for i in range(1,n+1):
            if i%3==0 and i%5==0:
                answer.append('FizzBuzz')
            elif i%3==0:
                answer.append('Fizz')
            elif i%5==0:
                answer.append('Buzz')
            else:
                answer.append(str(i))
        return answer