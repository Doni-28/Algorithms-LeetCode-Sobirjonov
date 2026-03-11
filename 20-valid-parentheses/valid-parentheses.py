class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        # стек для хранения открывающих скобок
        stack = []

        # словарь соответствия закрывающих и открывающих скобок
        pairs = {
            ')': '(',
            ']': '[',
            '}': '{'
        }

        # проходим по каждому символу строки
        for char in s:

            # если символ — открывающая скобка
            if char in pairs.values():
                stack.append(char)

            # если символ — закрывающая скобка
            else:
                # если стек пуст или тип скобок не совпадает
                if not stack or stack[-1] != pairs[char]:
                    return False

                # удаляем верхний элемент стека
                stack.pop()

        # если стек пуст — строка корректна
        return len(stack) == 0