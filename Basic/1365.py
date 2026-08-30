class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        # res = []
        # for i in nums:
        #     count = 0
        #     for j in nums:
        #         if j < i:
        #             count += 1
        #         else:
        #             continue
        #     res.append(count)
        # return res

        sorted_nums = sorted(nums)

        count = {}

        for i, num in enumerate(sorted_nums):
            if num not in count:
                count[num] = i

        return [count[num] for num in nums]
        