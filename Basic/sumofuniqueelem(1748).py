class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        freq_count = {}
        for num in nums:
            if num in freq_count:
                freq_count[num] += 1
            else:
                freq_count[num] = 1
        
        total = 0
        for key, value in freq_count.items():
            if value == 1:
                total += key
                
        return total