class Solution:
    def findComplement(self, num: int) -> int:
        
        mask=1<<(len(bin(num))-2)
        return (mask-1)^num
        
        mask=num
        mask|=mask>>1
        mask|=mask>>2
        mask|=mask>>4
        mask|=mask>>8
        mask|=mask>>16
        return num^mask
        
        
        # binary=list(bin(num)[2:])
        # for i in range(len(binary)):
        #     if binary[i]=='1':
        #         binary[i]='0'
        #     else:
        #         binary[i]='1'
        # return int(''.join(binary), 2)