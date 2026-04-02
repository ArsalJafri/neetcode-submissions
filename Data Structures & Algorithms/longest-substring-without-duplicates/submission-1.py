class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) < 2:
            return len(s)

        answer = 0
        left = 0
        right = 1
        mySet = set()
        mySet.add(s[left])

        while right < len(s):
            if s[right] not in mySet:
                mySet.add(s[right])
                right += 1
            else:
                answer = max(answer, len(mySet))
                while s[left] != s[right]:
                    mySet.remove(s[left])
                    left += 1
                left += 1
                right += 1
               

        return max(answer, len(mySet))
                





            


        