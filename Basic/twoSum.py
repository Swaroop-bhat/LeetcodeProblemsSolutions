class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        unique_nums = set()
        for num in range(len(nums)):
            diff = target - nums[num]

            if diff in unique_nums:
                return [num, nums.index(diff)]
            
            unique_nums.add(nums[num])