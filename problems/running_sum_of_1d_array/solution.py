class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        run_sum=[]
        sum_=0
        for i in nums:
            sum_+=i
            run_sum.append(sum_)
        return run_sum