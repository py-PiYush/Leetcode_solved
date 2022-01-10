class Solution:
    def partition(self, s: str) -> List[List[str]]:
    
        
        def isPalindrome(i,j):
            while i< j:
                if s[i]!=s[j]:
                    return False
                i+=1
                j-=1
            return True
        
        def helper(idx, res):
            if idx>=len(s):
                ans.append(res[:])
                return
            for i in range(idx, len(s)):
                if isPalindrome(idx, i):
                    helper(i+1, res+[s[idx:i+1]])
        
        ans=[]
        helper(0,[])
        return ans