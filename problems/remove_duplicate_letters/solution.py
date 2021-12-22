class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        last={c:i for i,c in enumerate(s)}
        stack=[]
        for i,c in enumerate(s):
            if c in stack: continue
            while stack and stack[-1]>c and i<last[stack[-1]]:
                print(stack)
                stack.pop()
            stack.append(c)
        return ''.join(stack)
                