class MyCircularQueue(object):

    def __init__(self, k):
        # размер очереди
        self.capacity = k
        
        # массив для хранения элементов
        self.queue = [0] * k
        
        # указатели
        self.front = 0
        self.rear = 0
        
        # текущее количество элементов
        self.size = 0


    def enQueue(self, value):
        if self.isFull():
            return False
        
        self.queue[self.rear] = value
        self.rear = (self.rear + 1) % self.capacity
        self.size += 1
        
        return True


    def deQueue(self):
        if self.isEmpty():
            return False
        
        self.front = (self.front + 1) % self.capacity
        self.size -= 1
        
        return True


    def Front(self):
        if self.isEmpty():
            return -1
        
        return self.queue[self.front]


    def Rear(self):
        if self.isEmpty():
            return -1
        
        return self.queue[(self.rear - 1) % self.capacity]


    def isEmpty(self):
        return self.size == 0


    def isFull(self):
        return self.size == self.capacity