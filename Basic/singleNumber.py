class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        freq_count = {}
        for i in nums:
            if i in freq_count:
                freq_count[i] += 1
            else:
                freq_count[i] = 1
        
        for key, value in freq_count.items():
            if value == 1:
                return key
        
        return None