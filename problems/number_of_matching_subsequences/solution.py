class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        
        d=defaultdict(list)
        cnt=0
        for word in words:
            d[word[0]].append(word)
        # print(d)
        for letter in s:
            arr=d[letter]
            d[letter]=[]
            # print(arr)
            for i in range(len(arr)):
                w=arr[i]
                # print(w)
                if len(w)==1:
                    cnt+=1
                else:
                    d[w[1]].append(w[1:])
        return cnt
        
        '''Brute Force (TLE)'''
        def checkSS(s1, s2):
            '''
            Check if s1 is subsequence of s2
            '''
            if len(s1)>len(s2): return False
            if not s1: return True
            
            i=j=0
            while i<len(s1) and j<len(s2):
                if s1[i]==s2[j]:
                    i+=1
                j+=1
            return i==len(s1)
        
        cnt=0
        for st in words:
            if checkSS(st, s):
                cnt+=1
        return cnt