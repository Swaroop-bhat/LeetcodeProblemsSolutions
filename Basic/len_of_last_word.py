class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        clean_str = s.strip()
        str_split = clean_str.split()
        return len(str_split[-1])
        