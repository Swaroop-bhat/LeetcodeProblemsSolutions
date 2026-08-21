class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        freq_count = {}
        for num in arr:
            if num in freq_count:
                freq_count[num] += 1
            else:
                freq_count[num] = 1
        
        unique_occurence = set()
        for key, value in freq_count.items():
            if value in unique_occurence:
                return False
            unique_occurence.add(value)
        return True
