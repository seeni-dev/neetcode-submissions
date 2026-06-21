class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str], ) -> int:
        return self.bfs(beginWord, endWord, wordList)
    def bfs(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        q = [beginWord]

        d = 1
        while q:
            nq = []
            for word in q:
                if word == endWord:
                    return d
        
                for i in range(len(word)):
                    for j in range(26):
                        ch = chr(ord('a')+j)
                        newWord = word[:i] + ch + word[i+1:]
                        if newWord in wordList:
                            nq.append(newWord)
                            wordList.remove(newWord)
            if nq:
                d +=1
            q = nq
        return 0