class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        """
        We iterate thru the array. When we find a number, we can push to stack.
        When we find a symbol, we need to pop an element from the stack. we do the
        operation with the popped element and the encountered symbol. we keep popping until
        empty.
        """

        total = 0
        nums = []
        for token in tokens:
            if token == "+":
                while nums:
                    num = nums.pop()
                    total += num
            
            elif token == "-":
                while nums:
                    num = nums.pop()
                    total -= num
                
            elif token == "*":
                while nums:
                    num = nums.pop()
                    total *= num
                
            elif token == "/":
                while nums:
                    num = nums.pop()
                    total //= num

            else:
                nums.append(int(token))

        return total