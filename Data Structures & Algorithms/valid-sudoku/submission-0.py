class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # initally, the approach that comes to mind is to
        # individually check if each rule is satisfied.
        # i can use a hashmap for O(1) checks for duplicates

        #first, we iterate through each list of strings.
        # when we encounter a number for the first time,
        # we can add it to our hashmap, otherwise, return False.

        #next, we iterate through each list of strings, but vertically.
        # we do the same thing. return False if duplicates.

        for row in board:
            nums = {}
            for char in row:
                if not char == ".":
                    if char in nums:
                        return False
                    else:
                        nums[char] = 1

        for col in range(9):
            nums = {}
            for row in board:
                char = row[col]
                if not char == ".":
                    if char in nums:
                        return False
                    else:
                        nums[char] = 1

        starts = [0, 3, 6]
        for r in starts:
            for c in starts:
                nums = {}
                for dr in [0, 1, 2]:
                    for dc in [0, 1, 2]:
                        char = board[r + dr][c + dc]
                        if not char == ".":
                            if char in nums:
                                return False
                            else:
                                nums[char] = 1
        
        return True
        
