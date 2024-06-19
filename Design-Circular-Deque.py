class MyCircularDeque:
    def __init__(self, k: int):
        self.q = [0] * k
        self.front = -1
        self.rear = -1
        self.capacity = k

    def insertFront(self, value: int) -> bool:
        if (self.front - self.rear) % self.capacity == 1:
            return False
        elif self.front == self.rear == -1:
            self.front = self.rear = 0
            self.q[self.front] = value
            return True
        else:
            self.front = (self.front - 1) % self.capacity
            self.q[self.front] = value
            return True

    def insertLast(self, value: int) -> bool:
        if (self.front - self.rear) % self.capacity == 1:
            return False
        elif self.front == self.rear == -1:
            self.front = self.rear = 0
            self.q[self.rear] = value
            return True
        else:
            self.rear = (self.rear + 1) % self.capacity
            self.q[self.rear] = value
            return True

    def deleteFront(self) -> bool:
        if self.front == -1:
            return False
        elif self.front == self.rear:
            self.front = self.rear = -1
            return True
        else:
            self.front = (self.front + 1) % self.capacity
            return True

    def deleteLast(self) -> bool:
        if self.front == -1:
            return False
        elif self.front == self.rear:
            self.front = self.rear = -1
            return True
        else:
            self.rear = (self.rear - 1) % self.capacity
            return True

    def getFront(self) -> int:
        if self.front == -1:
            return -1
        else:
            return self.q[self.front]

    def getRear(self) -> int:
        if self.rear == -1:
            return -1
        else:
            return self.q[self.rear]

    def isEmpty(self) -> bool:
        return self.front == -1

    def isFull(self) -> bool:
        return (self.front - self.rear) % self.capacity == 1


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()
