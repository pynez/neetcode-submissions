class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #this can be solved by first iterating through the list to create a
        #frequency list for each str in strs.

        # we have to cast the frequency list to a tuple bc hashmap keys cannot be mutable
        #we use that frequency list as a key in a hashmap. if the key already exists in the hashmap
        #we can append str to the value in the hashmap, otherwise, initialize a value as a list with
        #just str in it.
        seen = {}
        for s in strs:
            freqs = [0]*26
            for char in s:
                freqs[ord(char) - ord('a')] += 1
            freqs_tuple = tuple(freqs)
            if freqs_tuple in seen:
                seen[freqs_tuple].append(s)
            else:
                seen[freqs_tuple] = [s]

        return list(seen.values())

