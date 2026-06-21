class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        res = []
        characterLastIndices = {}
        for i, c in enumerate(s):
            characterLastIndices[c] = i

        partitionStart = 0
        partitionEnd = 0
        for i, c in enumerate(s):
            if i <= partitionEnd:
                partitionEnd = max(partitionEnd, characterLastIndices[c])
            else:
                res.append(partitionEnd - partitionStart + 1)
                partitionStart = i 
                partitionEnd = characterLastIndices[c]
        res.append(partitionEnd - partitionStart + 1)
        return res
        