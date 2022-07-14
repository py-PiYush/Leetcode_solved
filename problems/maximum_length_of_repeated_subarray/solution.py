class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        ''' Sliding window'''
        m = len(nums1)
        n = len(nums2)
        maxLen = 0
        
        for i in range(-(n-1), m):
            cnt = 0
            for j in range(n):
                if (i + j) < 0:
                    continue
                elif (i + j) >=m:
                    break
                elif nums1[i+j] == nums2[j]:
                    cnt = cnt + 1
                    maxLen = max(maxLen, cnt);
                else:
                    cnt = 0
        return maxLen
        
        
        ''' Tabulation '''
        m, n = len(nums1), len(nums2)
        dp = [[0 for _ in range(n+1)] for __ in range(m+1)]
        count = 0
        for i in range(1, m+1):
            for j in range(1, n+1):
                if nums1[i-1] == nums2[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                    count = max(count, dp[i][j])
                else:
                    dp[i][j] = 0
        return count
        
        ''' Memo '''
        @lru_cache(None)
        def lcs(i, j, count):
            if (i == 0 or j == 0):
                return count

            if (nums1[i - 1] == nums2[j - 1]):
                count = lcs(i - 1, j - 1, count + 1)

            count = max(count, max(lcs(i, j - 1, 0),
                                   lcs(i - 1, j, 0)))

            return count
        
        return lcs(len(nums1), len(nums2),0)
        
        
                    