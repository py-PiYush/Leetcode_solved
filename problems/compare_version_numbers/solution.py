class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        
        vr1_list = version1.split('.')
        vr2_list = version2.split('.')
        
        n1, n2 = len(vr1_list), len(vr2_list)
        if n1 < n2:
            vr1_list += ['0']*(n2-n1)
        elif n1 > n2:
            vr2_list += ['0']*(n1-n2)
            
        for x, y in zip(vr1_list, vr2_list):
            if int(x) < int(y):
                return -1
            if int(x) > int(y):
                return 1
        return 0