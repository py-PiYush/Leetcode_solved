class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        if len(bits)>1 and bits[-2]==0: return True
        
        i=0
        while i<len(bits):
            if bits[i]==0 and i==len(bits)-1:
                return True
            if bits[i]==1:
                i+=2
            else:
                i+=1
        return False