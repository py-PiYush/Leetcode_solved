class MyCircularQueue:

    def __init__(self, k: int):
        self.queue=[0]*k
        self.head,self.tail=-1,-1
        self.size=0
        self.max_size=k

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        if self.tail==-1:
            self.tail=self.head=0
        elif self.tail==self.max_size-1:
            self.tail=0
        else:
            self.tail+=1
        self.queue[self.tail]=value
        self.size+=1
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        if self.head==self.tail:
            self.head=self.tail=-1
        self.queue[self.head]=0
        self.head+=1
        if self.head>self.max_size-1:
            self.head=0
        self.size-=1
        return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.queue[self.head]
        

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.queue[self.tail]
        

    def isEmpty(self) -> bool:
        return self.size==0
        

    def isFull(self) -> bool:
        return self.size==self.max_size
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()