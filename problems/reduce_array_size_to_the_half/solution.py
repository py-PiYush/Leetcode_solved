from collections import OrderedDict
class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        count={}
        size=0
        for i in arr:
            if i in count:
                count[i]+=1
            else:
                count[i]=1
        count1=((sorted(count.keys(),key=lambda x:count[x],reverse=True)))
        i=0
        j=0
        while len(arr)-i>len(arr)/2:
            i+=count[count1[j]]
            j+=1
            size+=1
        return size
            
        
        