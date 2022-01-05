class Solution:
    def partition(self, s: str) -> List[List[str]]:
    
        
        def isPalindrome(x):
            i,j=0,len(x)-1
            while i< j:
                if x[i]!=x[j]:
                    return False
                i+=1
                j-=1
            return True
        
        def helper(idx, res):
            if idx>=len(s):
                ans.append(res[:])
                return
            for i in range(idx, len(s)):
                curString=s[idx:i+1]
                if isPalindrome(curString):
                    helper(i+1, res+[curString])
        
        ans=[]
        helper(0,[])
        return ans