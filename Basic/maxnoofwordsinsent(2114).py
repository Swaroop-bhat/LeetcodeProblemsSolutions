class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        count = 0
        for words in sentences:
            if count < words.count(' '):
                count = words.count(' ')
        return count + 1