class Solution:

    def encode(self, strs: List[str]) -> str:
        myList = []
        for i in strs:
            myList.append( str(len(i)) + ":" + i)
        return "".join(myList)

    
    def decode(self, s: str) -> List[str]:
        delimiter = ":"
        i = 0
        myList = []
        while i < len(s):
            j = s.index(":", i)  
            length = int(s[i:j])
            word = s[j+1:j+1+length] 
            myList.append(word)
            i = j + 1 + length
        return myList


