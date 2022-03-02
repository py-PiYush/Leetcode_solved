class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        cnt=Counter(arr1)
        res=[]
        srt=[]
        for i in arr2:
            res.extend([i]*cnt[i])
        for i in arr1:
            if i not in arr2:
                srt.append(i)
        srt.sort()
        return res+srt
    