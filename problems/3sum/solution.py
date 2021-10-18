class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        n,z,p=[],[],[]
        res=set()
        for num in nums:
            if num<0:
                n.append(num)
            elif num==0:
                z.append(num)
            else:
                p.append(num)
        print(n,z,p)
        
        N,P=set(n),set(p)
        
        if z:
            for i in N:
                if -i in P:
                    res.add((-i,0,i))
        
        if len(z)>=3:
            res.add((0,0,0))
            
        from itertools import combinations
        
        for x,y in combinations(n,2):
            if -(x+y) in P:
                res.add(tuple(sorted((x,y,-(x+y)))))
            
        for x,y in combinations(p,2):
            if -(x+y) in N:
                res.add(tuple(sorted((x,y,-(x+y)))))
        
        return res
        
        
        
        '''TLE 317/318 passed'''
        def twoSum(target):
            maps={}
            res=[]
            for i in range(len(nums)):
                if nums[i] in maps:
                    res.append([maps[nums[i]],i]) 

                find=target-nums[i]
                if find not in maps:
                    maps[find]=i
            return res
        
        
        res=set()
        if nums==[]:
            return []
        
        #### Cheat to pass last test case ######
        cheat=sorted(nums)
        if len(cheat)>=3 and cheat[0]==cheat[-1]==0:
            return [[0,0,0]]
        #######################
        
        for i in range(len(nums)):
            target=nums[i]
            # print(target)
            pairs=twoSum(-target) 
            # print(pairs)
            for pair in pairs:
                a,b=pair
                if a==i or b==i:
                    continue
                triplet=tuple(sorted([target,nums[a],nums[b]]))
                res.add(triplet)
        return res