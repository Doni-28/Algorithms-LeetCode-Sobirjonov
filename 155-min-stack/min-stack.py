class MinStack(object):

    def __init__(self):
        # основной стек
        self.stack = []
        
        # стек для хранения минимальных значений
        self.min_stack = []

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        
        # добавляем элемент в основной стек
        self.stack.append(val)

        # если стек минимумов пуст или новый элемент меньше текущего минимума
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)

    def pop(self):
        """
        :rtype: None
        """
        
        # удаляем верхний элемент
        val = self.stack.pop()

        # если удаляемый элемент является минимумом
        if val == self.min_stack[-1]:
            self.min_stack.pop()

    def top(self):
        """
        :rtype: int
        """
        
        # возвращаем верхний элемент стека
        return self.stack[-1]

    def getMin(self):
        """
        :rtype: int
        """
        
        # возвращаем текущий минимум
        return self.min_stack[-1]