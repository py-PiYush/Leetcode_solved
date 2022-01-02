


class ListNode:
    def __init__(self, key=-1, val=-1, next=None):
        self.key=key
        self.val=val
        self.next=next

class MyHashMap:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.buckets = 0xff
        self.maps = [[] for _ in range(self.buckets+1)]

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        index = key & self.buckets 
        
        for i, val in enumerate(self.maps[index]):
            if val[0] == key:
                self.maps[index][i][1] = value
                return
            
        self.maps[index].append([key, value])  

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        index = key & self.buckets 
        
        for val in self.maps[index]:
            if val[0] == key: return val[1]
            
        return -1

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        index = key & self.buckets 
        bucket = self.maps[index]
        
        for i, val in enumerate(bucket):
            if val[0] == key:
                if i < len(bucket)-1: bucket[i] = bucket[-1]
                bucket.pop()
                return

#     def __init__(self):
#         """
#         Initialize your data structure here.
#         """
#         self.size=1000
#         self.hash=[ListNode() for _ in range(self.size)]
    
#     def hashcode(self, key):
#         """
#         Encode the key to fit into current data structure
#         """
#         return key%self.size
        

#     def put(self, key: int, value: int) -> None:
#         """
#         value will always be non-negative.
#         """
#         hashcode=self.hashcode(key)
#         head=self.hash[hashcode]
#         while head.next:
#             if head.next.key==key:
#                 head.next.val=value
#                 return
#             head=head.next
#         head.next=ListNode(key, value)
        

#     def get(self, key: int) -> int:
#         """
#         Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
#         """
#         hashcode=self.hashcode(key)
#         head=self.hash[hashcode]
#         while head:
#             if head.key==key:
#                 return head.val
#             head=head.next
#         return -1
        

#     def remove(self, key: int) -> None:
#         """
#         Removes the mapping of the specified value key if this map contains a mapping for the key
#         """
#         hashcode=self.hashcode(key)
#         head=self.hash[hashcode]
#         while head.next:
#             if head.next.key==key:
#                 temp=head.next
#                 head.next=temp.next
#                 temp.next=None
#                 return
#             head=head.next


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)