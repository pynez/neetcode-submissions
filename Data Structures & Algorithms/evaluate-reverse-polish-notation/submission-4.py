class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        """
        We iterate thru the array. When we find a number, we can push to stack.
        When we find a symbol, we need to pop an element from the stack. we do the
        operation with the popped element and the encountered symbol. we keep popping until
        empty.
        """

        nums = []
        for token in tokens:
            if token == "+":
                num1 = nums.pop()
                num2 = nums.pop()
                nums.append(int(num1) + int(num2))
            
            elif token == "-":
                num1 = nums.pop()
                num2 = nums.pop()
                nums.append(int(num2) - int(num1))
                
            elif token == "*":
                num1 = nums.pop()
                num2 = nums.pop()
                nums.append(int(num1) * int(num2))
                
            elif token == "/":
                num1 = nums.pop()
                num2 = nums.pop()
                nums.append(int(num2/num1))

            else:
                nums.append(token)

        return nums[-1]