class Myqueue:
    def __init__(self,capacity):
        self.queue=[0]*capacity
        self.capacity=capacity
        self.front=0
        self.rear=0
    def enqueue(self,element):
        if self.isFull():
            print("queue is full,try later")
            return
        self.queue[self.rear]=element
        self.rear=self.rear+1
        print(f'added {element} successfully')
    def dequeue(self):
        if self.isEmpty():
            print('queue is empty.try later')
            return -1
        element=self.queue[self.front]
        self.front+=1
        print(f'removed {element} successfully')
        return element
    def size(self):
        return self.rear-self.front

    def isFull(self):
        if self.rear==self.capacity:
            return True
        else:
            return False

    def isEmpty(self):
        if self.front==self.rear:
            return True
        else:
            return False
    def peek(self):
        if self.isEmpty():
            print("it is error")

    def display(self):
        if self.isEmpty():
            print("Queue is Empty")
        else:
            print("Queue Elements:", self.queue[self.front:self.rear])


q=Myqueue(5)
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.display()
q.dequeue()
q.display()