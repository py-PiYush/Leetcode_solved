class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        
        '''Using counter'''
        # cnt=Counter(nums)
        # maj=len(nums)//3
        # return [n for n in cnt if cnt[n]>maj]
        
        
        '''Boyer moore voting algo'''
        if not nums:
            return []
        count1, count2, candidate1, candidate2 = 0, 0, 0, 1
        for n in nums:
            if n == candidate1:
                count1 += 1
            elif n == candidate2:
                count2 += 1
            elif count1 == 0:
                candidate1, count1 = n, 1
            elif count2 == 0:
                candidate2, count2 = n, 1
            else:
                count1, count2 = count1 - 1, count2 - 1
        return [n for n in (candidate1, candidate2)
                    if nums.count(n) > len(nums) // 3]
        
        
        def findCandidates():
            can1, can2 = -1, -1
            cnt1, cnt2 = 0, 0
            for num in nums:
                if num==can1:
                    cnt1+=1
                elif num==can2:
                    cnt2+=1
                elif cnt1==0:
                    can1, cnt1 = num, 1
                elif cnt2==0:
                    can2, cnt2= num, 1
                else:
                    cnt1-=1
                    cnt2-=1
            return [can1] if can1==can2 else [can1, can2]
        
        def isMajority(can):
            cnt=0
            maj=len(nums)//3
            for num in nums:
                if num==can:
                    cnt+=1
            return cnt>maj
        
        def boyer_moore():
            candidates = findCandidates()
            print(candidates)
            res=[]
            for candidate in candidates:
                if isMajority(candidate):
                    res.append(candidate)
            return res
        
        return boyer_moore()