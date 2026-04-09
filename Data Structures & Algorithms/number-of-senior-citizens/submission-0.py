class Solution:
    def countSeniors(self, details: List[str]) -> int:
        counter = 0
        for i in range(len(details)):
            age = int(details[i][11] + details[i][12])
            if age > 60:
                counter += 1

        return counter