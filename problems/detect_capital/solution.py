class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        
        ''' inbuilt libraries'''
        return word.isupper() or word.islower() or word.istitle()
        
        
        
        
        
        def checkAll(idx, case):
            if case=='lower':
                for i in range(idx, len(word)):
                    if 'a'<=word[i]<='z':
                        continue
                    else:
                        return False
            if case=='upper':
                for i in range(idx, len(word)):
                    if 'A'<=word[i]<='Z':
                        continue
                    else:
                        return False
            return True
        
        if 'A'<=word[0]<='Z':
            return checkAll(1, 'upper') or checkAll(1, 'lower')
        if 'a'<=word[0]<='z':
            return checkAll(1, 'lower')