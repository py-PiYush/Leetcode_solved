class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        ''' using queue to form sequential integer'''
        queue=collections.deque(range(1,10))
        res=[]
        while queue:
            num=queue.popleft()
            if low<=num<=high:
                res.append(num)
            
            last=num%10
            if last<9:
                queue.append(num*10 +last+1)
        return res
        
        
        
        ''' ;)'''
        l=[12,23,34,45,56,67,78,89,123,234,345,456,567,678,
           789,1234,2345,3456,4567,5678,6789,12345,23456,
           34567,45678,56789,123456,234567,345678,456789,
           1234567,2345678,3456789,12345678,23456789,123456789]
        
        ans = []
        for li in l:
            if li >= low and li <= high: 
                ans.append(li)
        return ans
        
        
        
        ''' sliding windows of all existing sizes (type casting)'''
        l, h=len(str(low)), len(str(high))
        s='123456789'
        res=[]
        for i in range(l, h+1):
            left, right = 0, i-1
            while right<len(s):
                num=int(s[left:right+1])
                if num<=high and num>=low:
                    res.append(num)
                elif num>high:
                    break
                left+=1
                right+=1
        return res
        

        
        ''' brute force '''
        def sequential(num):
            s=str(num)
            for i in range(1, len(s)):
                if int(s[i])-1 != int(s[i-1]):
                    return False
            return True
        
        res=[]
        for n in range(low, high+1):
            if sequential(n):
                res.append(n)
        return res