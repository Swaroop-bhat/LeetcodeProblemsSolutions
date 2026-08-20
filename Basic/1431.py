class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_elem = max(candies)
        result = []
        for cand in candies:
            if cand + extraCandies >= max_elem:
                result.append(True)
            else:
                result.append(False)
        return result