class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        alpha=list('abcdefghijklmnopqrstuvwxyz')
        morph=[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        mapp=dict(zip(alpha,morph))
        res=set()
        for i in words:
            res.add(''.join([mapp[j] for j in i]))
        return len(res)