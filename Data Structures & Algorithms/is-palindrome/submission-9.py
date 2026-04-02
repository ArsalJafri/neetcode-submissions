class Solution:
    def isPalindrome(self, s: str) -> bool:
      #two pointer algorithm
      left = 0
      right = len(s) - 1  
      while left < right:
        if s[left].isalnum() == False:
            left += 1
            continue
        if s[right].isalnum() == False:
            right -= 1
            continue
        if s[left].lower() != s[right].lower():
            print(s[left])
            print(s[right])
            return False
        left +=1
        right -=1

      return True