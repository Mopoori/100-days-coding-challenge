class MyStack:
    def __init__(self,capacity):
        self.stack=[0] * capacity
        self.top=-1
        self.capacity=capacity
    def isEmpty(self):
        return self.top==-1
    def isFull(self):
        return self.top==self.capacity-1
    def push(self,element):
        if (self.top==self.capacity-1):
            print("over floe stack")
            return
        self.top=self.top+1
        self.stack[self.top]=element
    def pop(self):
        if self.isEmpty():
            print('stack under flow')
            return -1
        element=self.stack[self.top]
        self.top=self.top-1
        return element
    def peek(self):
        if self.isEmpty():
            print('stack is empty')
            return None
        return self.stack[self.top]
    def display(self):
        if self.isEmpty():
            print("stack is empty")
            return
        for i in range(self.top,-1,-1):
            print(self.stack[i],end=' ')
        print()


m=MyStack(5)
m.push(10)
m.push(20)
m.display()
print(m.pop())
print(m.isEmpty())
print(m.isFull())
print(m.peek())