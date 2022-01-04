class Solution:
    def bitwiseComplement(self, n: int) -> int:
        binary=list(bin(n)[2:])
        for i in range(len(binary)):
            if binary[i]=='1':
                binary[i]='0'
            else:
                binary[i]='1'
        return int(''.join(binary), 2)