class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        rev = []
        for img in image:
            a = []
            for i in img:
                if i == 0:
                    a.append(1)
                else:
                    a.append(0)
            rev.append(a)
        res = []
        for i in rev:
            res.append(i[::-1])
        return res
            

