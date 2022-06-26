class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)
        if k==n: return sum(cardPoints)

        cur_sum = sum(cardPoints[:n-k])
        # print(cur_sum)
        min_sum_k = cur_sum
        for i in range(n-k,n):
            cur_sum+= cardPoints[i]-cardPoints[i-n+k]
            min_sum_k= min(min_sum_k, cur_sum)
        # print(min_sum_k)
        
        return sum(cardPoints) - min_sum_k