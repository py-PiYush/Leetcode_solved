class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        uniq=set()
        for email in emails:
            res=''
            skip=0
            local=1
            for c in email:
                if c== '@':
                    skip = 0
                    local=0
                if (c == '.' and local) or skip: continue
                if c=='+':
                    skip = 1
                    continue
                
                res+=c
            print(res)
            uniq.add(res)
            
        return len(uniq)