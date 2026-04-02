class Solution:

    def encode(self, strs: List[str]) -> str:
        string = ""
        for i in range(len(strs)):
            size = len(strs[i])
            string += str(size) + '#' + strs[i] 
        print(string)
        return string

    def decode(self, s: str) -> List[str]:
        array = []
        #two pointer scan
        i = 0
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            length = s[i:j] #Length
            length = int(length)
            decode = s[j+1 : j + length  + 1 ]
            array.append(decode)
            i =  j + length  + 1

        return array
        
