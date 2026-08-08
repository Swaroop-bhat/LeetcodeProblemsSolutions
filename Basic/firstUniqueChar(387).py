class Solution:
    def firstUniqChar(self, s: str) -> int:
        freq_count = {}
        for char in s:
            if char in freq_count:
                freq_count[char] += 1
            else:
                freq_count[char] = 1
        
        for i in range(len(s)):
            if freq_count[s[i]] == 1:
                return i
        
        return -1