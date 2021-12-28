class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        def generate(p, left, right, parens=[]):
            if left:         generate(p + '(', left-1, right)
            if right > left: generate(p + ')', left, right-1)
            if not right:    parens += p,
            return parens
        return generate('', n, n)
        
#         def helper(S=[], l=0, r=0):
#             if len(S)==2*n:
#                 ans.append(''.join(S))
#                 return
            
#             if l<n:
#                 S.append('(')
#                 helper(S,l+1, r)
#                 S.pop()
#             if r<l:
#                 S.append(')')
#                 helper(S,l,r+1)
#                 S.pop()
        
#         ans=[]
#         helper()
#         return ans
                