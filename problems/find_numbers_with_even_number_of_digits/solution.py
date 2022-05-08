class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        
        def countDigits(n):
            cnt=0
            while n:
                n//=10
                cnt+=1
            return cnt
        
        return len([i for i in map(countDigits, nums) if i%2==0])
        
        
        '''typecast'''
        new=map(str,nums)
        return len([len(i) for i in new if len(i)%2==0])
        