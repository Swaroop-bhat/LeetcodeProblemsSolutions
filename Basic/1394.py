class Solution:
    def findLucky(self, arr: List[int]) -> int:
        freq_count = {}
        for i in arr:
            if i in freq_count:
                freq_count[i] += 1
            else:
                freq_count[i] = 1
        
        print(freq_count)
        
        res = -1
        for key, value in freq_count.items():
            if key == value and key > res:
                res = key
        return res