class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        dictionary = {}
        for words in strs:
            key = "".join(sorted(words))
            if key not in dictionary:
                dictionary[key] = []
            dictionary[key].append(words)

        return list(dictionary.values())
        
