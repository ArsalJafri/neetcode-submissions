class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.replace(" ", "")
        s = s.replace("?", "")
        s = s.replace("!", "")
        s = s.replace(".", "")
        s = s.replace("'", "")
        s = s.replace(",", "")
        s = s.replace(":", "")
        s = s.lower()
        

        return s[::-1] == s
        