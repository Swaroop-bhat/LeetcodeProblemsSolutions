class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # for i in nums:
        #     if nums.count(i)>1:
        #         nums.remove(i)
        # return len(nums)


        if len(nums) == 0:
            return 0

        write = 0

        for read in range(1, len(nums)):
            if nums[read] != nums[write]:
                write += 1
                nums[write] = nums[read]

        return write + 1
        