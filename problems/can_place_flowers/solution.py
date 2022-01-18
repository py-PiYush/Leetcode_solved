class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        l=len(flowerbed)+2
        bed=[0]+flowerbed+[0]
        
        for i in range(1, l-1):
            if bed[i]==bed[i-1]==bed[i+1]==0:
                bed[i]=1
                n-=1
            if n==0:
                break
        return n<=0