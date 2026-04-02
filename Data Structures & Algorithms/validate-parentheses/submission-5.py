class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for i in range(len(s)):
            if len(stack) == 0:
                if s[i] == "]" or s[i] == "}" or s[i] == ")":
                    return False
            if s[i] == "(" or s[i] == "[" or s[i] == "{":
                stack.append(s[i])
            if s[i] == ")":
                if stack[-1] == "(":
                    stack.pop()
                else:
                    return False
            if s[i] == "]":
                if stack[-1] == "[":
                    stack.pop()
                else:
                    return False
            if s[i] == "}":
                if stack[-1] == "{":
                    stack.pop()
                else:
                    return False
        
        return len(stack) == 0
        