class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        res = []

        for word in words:
            for j in words:
                if word in j and word != j and word not in res:
                    res.append(word)

        return res
        