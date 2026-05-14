class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #The solution would be to create lists for each string
        #the lists have the frequency of each letter
        #is s and t are anagrams, their lists are identical.

        s_frequencies = [0]*26
        for char in s:
            s_frequencies[ord(char) - ord("a")] += 1

        t_frequencies = [0] * 26
        for char in t:
            t_frequencies[ord(char) - ord("a")] += 1

        return (s_frequencies == t_frequencies)