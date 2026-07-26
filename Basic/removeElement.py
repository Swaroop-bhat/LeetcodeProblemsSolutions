class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # n=nums
        # for i in n:
        #     if i==val:
        #         nums.remove(i)
        # return len(nums)
        write = 0
        for read in range(len(nums)):
            if nums[read] != val:
                nums[write] = nums[read]
                write += 1
                
        return write



        