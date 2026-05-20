class Solution:
    def get_character_count(self, strs) -> [List[int]]:
        res = [0 for i in range(26)]
        for ch in strs:
            res[ord(ch) - ord('a')] +=1
        return res

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        for word in strs:
            character_count = self.get_character_count(word)
            groups[tuple(character_count)] = groups.get(tuple(character_count), []) + [word]
        return list(groups.values())
        