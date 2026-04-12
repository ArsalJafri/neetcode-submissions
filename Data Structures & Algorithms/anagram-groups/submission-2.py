class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = defaultdict(list)

        for word in strs:
            count = [0] * 26
            for character in word:
                index = ord(character) - ord('a')
                count[index] += 1
            hashmap[ tuple(count) ].append(word)
        
        return list(hashmap.values())
            