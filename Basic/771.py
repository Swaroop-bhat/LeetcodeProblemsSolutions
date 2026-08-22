class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        unique_set = set(jewels)
        res = 0
        for stone in stones:
            if stone in unique_set:
                res += 1
        return res