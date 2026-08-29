class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        prev_count = 0
        curr_count = 0
        for num in nums:
            if num == 1:
                curr_count += 1
            
            if num == 0:
                curr_count = 0
            
            if curr_count > prev_count:
                prev_count = curr_count

        return prev_count

            