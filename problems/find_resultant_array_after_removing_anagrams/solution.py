class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        def isAnagram(s1, s2):
            return Counter(s1)==Counter(s2)
        
        res = []
        i, j = 0, 1
        while i<len(words):
            while j<len(words) and isAnagram(words[i], words[j]):
                j+=1
            res.append(words[i])
            i=j
        return res
            