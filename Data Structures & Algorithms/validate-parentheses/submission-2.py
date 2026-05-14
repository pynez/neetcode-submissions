class Solution:
    def isValid(self, s: str) -> bool:
        #for this solution we can implement a stack
        #because of the LIFO nature of the stack, when we read
        #an opening bracket, we can append a closing bracket to 
        #the stack. when we read a closing bracket, we can pop
        #from the stack and if the popped element matches the 
        #element read, then we continue, if it doesn't match we can
        #return false
        #at the end of iteration if the stack is not empty, it means
        #we read more opening brackets than closing brackets and we 
        #can return false.

        stack = []
        #let's also implement a map just to make things a tad easier
        brackets  = {"(": ")", "[": "]", "{": "}"}
        for char in s:
            if char in brackets:
                stack.append(brackets[char])
            elif not stack:
                return False
            elif stack.pop() != char:
                return False
        
        if stack:
            return False
        return True