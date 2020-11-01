class Solution:
    def complexNumberMultiply(self, a: str, b: str) -> str:
        A=[int(x) for x in a.replace('i','').split('+')]
        B=[int(x) for x in b.replace('i','').split('+')]
        real=A[0]*B[0]-A[1]*B[1]
        img=A[0]*B[1]+A[1]*B[0]
        return str(real)+'+'+str(img)+'i'
        