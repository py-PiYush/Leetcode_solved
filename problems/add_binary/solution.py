class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        carry=0
        res=''
        a,b=map(list, (a,b))
        while a or b or carry:
            if a:
                carry+=int(a.pop())
            if b:
                carry+=int(b.pop())
            res+=str(carry%2)
            carry//=2
        
        return res[::-1]