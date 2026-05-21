class Solution:

    def encode_str(self, s) -> str:
        return f"{len(s)}_{s}"

    def encode(self, strs: List[str]) -> str:
        r = [self.encode_str(s) for s in strs]
        return str(len(strs)) + "_" + ''.join(r)
    
    def read_until(self, s: str, i: int, until_ch: str):
        res = []
        while s[i] != until_ch:
            res.append(s[i])
            i+=1
        i+=1
        return [''.join(res), i]
    
    def read_n(self, s: str, i: int, num: int):
        return [s[i:i+num], i+num]
    
    def decode(self, s: str) -> List[str]:
        print(s)
        token, i = self.read_until(s, 0, "_")
        print(token, i)
        r = []
        for _ in range(int(token)):
            token, i = self.read_until(s, i, "_")
            word, i = self.read_n(s, i, int(token))
            print(token, i, word)
            r.append(word)
        return r
