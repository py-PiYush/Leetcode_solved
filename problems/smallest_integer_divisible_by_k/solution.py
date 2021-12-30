class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        if k%10 not in {1,3,7,9}: return -1
        
        mod,seen=0,set()
        for length in range(1,k+1):
            mod=(mod*10+1)%k
            if mod==0:
                return length
            if mod in seen:
                return -1
            seen.add(mod)
        return -1
            
        