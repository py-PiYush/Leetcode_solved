class Solution:
    def minimumNumbers(self, num: int, k: int) -> int:
        arr=[]
        for n in range(1,num+1):
            if n%10 == k:
                arr.append(n)
        
        # print(arr)
        if num==0:
            return 0
        dp=[0]+[float('inf')]*num
        for n in arr:
            for i in range(n, num+1):
                dp[i]=min(dp[i], 1 + dp[i-n])
        # print(dp)
        return dp[num] if dp[num]!=float('inf') else -1