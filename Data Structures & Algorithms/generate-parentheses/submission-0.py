class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        answer = []

        def backtracker(enter, close, total):
            
            if enter > n or close > n or close > enter:
                return 
            
            if enter == n and close == n:
                answer.append(total)
                return
                
            if enter < n:
                backtracker(enter+1, close, total + "(" )

            if close < n:
                backtracker(enter, close+1,  total + ")" )

            

        backtracker(0,0,"")
        return answer
