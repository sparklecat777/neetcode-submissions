class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        def extractStack() -> float:
            b = stack.pop()
            a = stack.pop()
            return a,b
        
        stack = []
        for i in range(len(tokens)):
            try: 
                stack.append(int(tokens[i]))
            except: 
                if tokens[i] == "+":
                    x1, x2 = extractStack()
                    stack.append(x1 + x2)
                elif tokens[i] == "*":
                    x1, x2 = extractStack()
                    stack.append(x1 * x2)
                elif tokens[i] == "-":
                    x1, x2 = extractStack()
                    stack.append(x1 - x2)
                elif tokens[i] == "/":
                    x1, x2 = extractStack()
                    stack.append(int(x1 / x2))
        return int(stack.pop())


         

            
