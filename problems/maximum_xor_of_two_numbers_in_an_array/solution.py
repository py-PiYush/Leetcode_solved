class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        ans, mask = 0, 0
        for i in range(31, -1, -1):
            mask |= 1<<i
            found = set([num & mask for num in nums])
                
            start = ans | 1<<i
            for pref in found:
                if start^pref in found:
                    ans = start
                    break
        return ans
        
        
        
    
        answer = 0
        for i in range(32)[::-1]:
            answer <<= 1
            prefixes = {num >> i for num in nums}
            answer += any(answer^1 ^ p in prefixes for p in prefixes)
        return answer

        
        
        ''' Brute force O(n^2)'''
        maxXor=0
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                maxXor = max(maxXor, nums[i]^nums[j])
        return maxXor