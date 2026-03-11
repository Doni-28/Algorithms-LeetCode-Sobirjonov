class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """

        stack = []

        for token in tokens:

            # если элемент не оператор — это число
            if token not in ["+", "-", "*", "/"]:
                stack.append(int(token))

            else:
                # извлекаем два последних числа
                b = stack.pop()
                a = stack.pop()

                # выполняем операцию
                if token == "+":
                    stack.append(a + b)

                elif token == "-":
                    stack.append(a - b)

                elif token == "*":
                    stack.append(a * b)

                elif token == "/":
                    # деление с усечением к нулю
                    stack.append(int(float(a) / b))

        # результат остаётся в стеке
        return stack[0]