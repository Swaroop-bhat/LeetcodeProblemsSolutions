class Solution:
    def repeatedCharacter(self, s: str) -> str:
        unique_set = set()
        for ch in s:
            if ch in unique_set:
                return ch
            unique_set.add(ch)
        
        return None
        