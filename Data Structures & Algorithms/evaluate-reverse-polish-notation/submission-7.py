class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        answer = 0

        for i in range(len(tokens)):
            if tokens[i] == "+":
                top = stack[-1]
                top2 = stack[-2]
                stack.pop()
                stack.pop()
                answer = top + top2
                stack.append(answer)
            elif tokens[i] == "*":
                top = stack[-1]
                top2 = stack[-2]
                stack.pop()
                stack.pop()
                answer = top * top2
                stack.append(answer)
            elif tokens[i] == "-":
                top = stack[-1]
                top2 = stack[-2]
                stack.pop()
                stack.pop()
                answer = top2 - top
                stack.append(answer)
            elif tokens[i] == "/":
                top = stack[-1]
                top2 = stack[-2]
                stack.pop()
                stack.pop()
                answer = int(top2 / top)
                stack.append(answer)
            else:
                stack.append(int(tokens[i]))
                print(stack)
               
        

        return int(stack[0])
            
