class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str], ) -> int:
        return self.bfs(beginWord, endWord, wordList)
    def bfs(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        q = [[beginWord, set([beginWord])]]

        while q:
            nq = []
            for word, path in q:
                print(word, path)
                if word == endWord:
                    print(path)
                    return len(path)
        
                for i in range(len(word)):
                    for j in range(26):
                        ch = chr(ord('a')+j)
                        newWord = word[:i] + ch + word[i+1:]
                        if newWord in wordList and newWord not in path:
                            nq.append([newWord, path | set([newWord])])
            q = nq
        return 0