class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_map = [0] * 26
        for ch in s1:
            s1_map[ord(ch) - ord('a')] += 1
        window_start = 0  
        i = 0      
        s2_map = [0] * 26        
        while i < len(s2):
            left_ch = s2[window_start]
            right_ch = s2[i]
            s2_map[ord(right_ch) - ord('a')] +=1
            if (i - window_start +1) == len(s1):
                if s1_map == s2_map:
                    return True
                s2_map[ord(left_ch) -ord('a')] -=1
                window_start +=1
            i += 1
        return False
                

        