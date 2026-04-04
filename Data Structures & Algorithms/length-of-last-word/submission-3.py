class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        if len(s) == 1:
            return len(s)

        counter = 0
        i = len(s) - 1

        if s[i] == " ":
            while s[i] == " ":
                i -= 1
        if s[i] != " ":
            while s[i] != " ":
                counter += 1
                i -= 1
        
        return counter

                 