class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        max_elem_to_right = arr[-1]
        arr[-1] = -1
        i = len(arr)-2
        
        while i >= 0:
            if arr[i] > max_elem_to_right:
                arr[i], max_elem_to_right = max_elem_to_right, arr[i]
            else:
                arr[i] = max_elem_to_right
            
            i-=1
            
        return arr