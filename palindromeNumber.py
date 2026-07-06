class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        i = 0
        j = len(str(x)) - 1
        y = str(x)
        while i < j:
            if y[i] != y[j]:
                return False
            
            i += 1
            j -= 1

        return True
