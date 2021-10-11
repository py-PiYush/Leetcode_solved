class Solution:
    def isValid(self, s: str) -> bool:
        opp={'(':')','{':'}','[':']'}
        stack=[]
        i=0
        while i<len(s):
            if s[i] in opp:
                stack.append(s[i])
            else:
                left=stack.pop() if stack else None
                if not left or opp[left]!=s[i]:
                    return False
            i+=1
        return True if not stack else False
            
                
        