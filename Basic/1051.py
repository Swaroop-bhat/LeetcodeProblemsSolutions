class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        sorted_list = sorted(heights)
        print(sorted_list)

        res = 0
        for i in range(len(heights)):
            if heights[i] != sorted_list[i]:
                res += 1
        return res