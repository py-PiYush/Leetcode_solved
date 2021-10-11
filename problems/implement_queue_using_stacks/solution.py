class MyQueue:

    def __init__(self):
        self.newStack=[]
        self.oldStack=[]
        
    def shift(self):
        if self.oldStack==[]:
            while len(self.newStack):
                self.oldStack.append(self.newStack.pop())

    def push(self, x: int) -> None:
        self.newStack.append(x)

    def pop(self) -> int:
        if self.empty():
            return False
        self.shift()
        return self.oldStack.pop()

    def peek(self) -> int:
        if self.empty():
            return False
        self.shift()
        return self.oldStack[-1]

    def empty(self) -> bool:
        return len(self.newStack)+len(self.oldStack)==0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()