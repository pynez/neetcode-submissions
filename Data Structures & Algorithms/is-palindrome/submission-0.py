class Solution:
    def isPalindrome(self, s: str) -> bool:
        # we can use a 2 pointer method to achieve this in O(n) time.
        # before we do this, we have to normalize the string.

        normal_s = ""
        for char in s:
            if char.isalnum():
                normal_s += (char)

        normal_s = normal_s.casefold()

        l = 0
        r = len(normal_s) - 1

        while l < r:
            matched = normal_s[l] == normal_s[r]
            if not matched:
                return False
            l += 1
            r -= 1
        return True