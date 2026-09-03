class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        # word_count = 0
        # res = ""
        # s_split = s.split()
        # while word_count < k:
        #     res += s_split[word_count]
        #     word_count += 1
        #     if word_count < k:
        #         res += " "
        # return res

        return " ".join(s.split()[:k])