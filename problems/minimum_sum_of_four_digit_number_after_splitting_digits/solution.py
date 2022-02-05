class Solution:
    def minimumSum(self, num: int) -> int:
        heap, n = [], num
        while n > 0: # Push all digits of num into heap
            heappush(heap,  n % 10)
            n = n // 10
        nums1 = nums2 = 0
        while len(heap) > 0: # Use smallest digits to construct each number
            v1 = heappop(heap)
            nums1 = nums1 * 10 + v1
            if len(heap) > 0:
                v2 = heappop(heap)
                nums2 = nums2 * 10 + v2
        return nums1 + nums2
        
        
        
        '''-----------------------------------'''
        s=sorted(str(num))
        s1=''.join(s[::2])
        s2=''.join(s[1::2])
        # print(s1, s2)
        return int(s1)+int(s2)