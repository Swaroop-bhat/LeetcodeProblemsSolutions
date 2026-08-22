class Solution:
    def reverseWords(self, s: str) -> str:
        s_list = s.split()
        rev_word = []

        for ch in s_list:
            rev_word.append(ch[::-1])

        return " ".join(rev_word)