class Solution:
    def isPalindrome(self, palindrome: str)->str:
        if palindrome[::-1]==palindrome:
            return True
        return False
    
    def breakPalindrome(self, palindrome: str) -> str:
        if len(palindrome)==1:
            return ''
        lst=list(palindrome)
        for i in range(len(palindrome)):
            if lst[i]!='a':
                lst[i]='a'
                break
        new_p=''.join(lst)
        if self.isPalindrome(new_p):
            return palindrome[:-1]+'b'
        else:
            return new_p
            
        
        