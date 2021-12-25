class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        maxCount=0
        for sentence in sentences:
            spaceCount=0
            for word in sentence:
                if word==' ':
                    spaceCount+=1
            maxCount=max(maxCount,spaceCount)
        return maxCount+1