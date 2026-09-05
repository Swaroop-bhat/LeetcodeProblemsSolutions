class Solution:
    def calPoints(self, operations: List[str]) -> int:
        res = []
        for operation in operations:
            print(res)
            if operation == "+":
                ttl = sum([res[-1], res[-2]])
                res.append(ttl)
            elif operation == "C":
                res.remove(res[-1])
            elif operation == "D":
                mul = 2*res[-1]
                res.append(mul)
            else:
                res.append(int(operation))
        
        return sum(res)