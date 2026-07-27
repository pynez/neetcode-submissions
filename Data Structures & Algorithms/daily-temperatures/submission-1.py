class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        '''
        we want to maintain a monotonically decreasing stack to find days where the temperature is higher.

        PLAN:
        1. Instantiate an empty stack.
        2. Instantiate an array of length temperatures. Every element is instantiated to the default value, 0
        3. Iterate through temperatures:
            1a. If the stack is empty, push temperature to stack
            1b. Else, compare the top of the stack with temperature:
            2a. If temperature is less than or equal to the peeked element, push temperature to the stack
            2b. Else, while temperature > stack head
            2b. Else, the number of days before the a warmer day for the top of the stack is the index of
                the peeked element - the index of temperature.
        '''

        stack = []
        out = [0] * len(temperatures)

        for i in range(len(temperatures)):
            while stack and temperatures[stack[-1]] < temperatures[i]:
                index = stack.pop()
                out[index] = i - index
            stack.append(i)

        return out
