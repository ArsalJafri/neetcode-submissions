class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if len(tokens) == 1:
            return int(tokens[0])
        stack = []

        for i in range(len(tokens)):
            if tokens[i] == "+":
                x = int(stack.pop())
                y = int(stack.pop())
                stack.append((x+y))

            elif tokens[i] == "-":
                x = int(stack.pop())
                y = int(stack.pop())
                stack.append((y-x))

            elif tokens[i] == "*":
                x = int(stack.pop())
                y = int(stack.pop())
                stack.append((x * y))

            elif tokens[i] == "/":
                x = int(stack.pop())
                y = int(stack.pop())
                stack.append((y / x))

            else:
                stack.append(tokens[i])

            print(stack)

        print(stack)

        return math.floor(stack[-1])

