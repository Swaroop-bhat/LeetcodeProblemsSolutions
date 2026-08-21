class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        count = 0
        for i in nums:
            j = str(i)
            if len(j) % 2 == 0:
                count += 1
            else:
                continue
        return count
        