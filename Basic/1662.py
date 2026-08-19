class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        res_1 = ""
        for word in word1:
            res_1 += word

        res_2 = ""
        for word in word2:
            res_2 += word
        
        return res_1 == res_2
        