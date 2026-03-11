class MyQueue(object):

    def __init__(self):
        # стек для добавления элементов
        self.stack_in = []

        # стек для извлечения элементов
        self.stack_out = []

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.stack_in.append(x)

    def pop(self):
        """
        :rtype: int
        """

        # если стек извлечения пуст — переносим элементы
        if not self.stack_out:
            while self.stack_in:
                self.stack_out.append(self.stack_in.pop())

        return self.stack_out.pop()

    def peek(self):
        """
        :rtype: int
        """

        if not self.stack_out:
            while self.stack_in:
                self.stack_out.append(self.stack_in.pop())

        return self.stack_out[-1]

    def empty(self):
        """
        :rtype: bool
        """

        return not self.stack_in and not self.stack_out