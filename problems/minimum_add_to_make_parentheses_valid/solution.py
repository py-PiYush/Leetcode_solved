class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        
        bal = ans = 0
        for ch in s:
            bal += 1 if ch=='(' else -1
            if bal==-1:
                ans+=1
                bal+=1
        return ans+bal
        
        
        
        
        '''---------2-----------'''
        left, right = [], []
        for i,ch in enumerate(s):
            if ch=='(':
                left.append(i)
            else:
                if left:
                    left.pop()
                else:
                    right.append(i)
        return len(left)+len(right)
        
        '''-------------3------------'''
        marked = [False]*len(s)
        left = []
        for i,ch in enumerate(s):
            if ch=='(':
                left.append(i)
            else:
                if left:
                    marked[i]=True
                    marked[left.pop()]=True
        return sum(1 for b in marked if b==False)
                