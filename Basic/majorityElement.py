class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        freq_count = {}
        # nums_len = len(nums)
        # for i in nums:
        #     if i in freq_count:
        #         freq_count[i] += 1
        #     else:
        #         freq_count[i] = 1
        
        # for key, value in freq_count.items():
        #     if value > (nums_len / 2):
        #         return key
        candidate = None
        count = 0

        for num in nums:
            if count == 0:
                candidate = num

            if num == candidate:
                count += 1
            else:
                count -= 1

        return candidate
        
