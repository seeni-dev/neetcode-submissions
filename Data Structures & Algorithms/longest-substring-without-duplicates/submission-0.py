class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window_start = 0
        dictionary = {}
        max_substring_length = 0
        for i, ch in enumerate(s):
            if ch in dictionary and dictionary[ch] >= window_start:
                window_start = dictionary[ch] + 1
            dictionary[ch] = i
            max_substring_length = max(max_substring_length, i - window_start + 1)
        return max_substring_length