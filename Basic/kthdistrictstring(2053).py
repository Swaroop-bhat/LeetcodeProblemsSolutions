class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        # count = 0
        # for ch in arr:
        #     if arr.count(ch) == 1:
        #         count += 1

        #     if count == k:
        #         return ch

        # return ""
        freq_count = {}
        for ch in arr:
            if ch in freq_count:
                freq_count[ch] += 1
            else:
                freq_count[ch] = 1
        
        count = 0
        for key, value in freq_count.items():
            if value == 1:
                count += 1
            
            if count == k:
                return key
        return ""