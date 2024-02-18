# count and Say
class Solution:
    def countAndSay(self, n: int) -> str:
        def evaluate(s):
            i = 0
            res = []
            while i < len(s):
                number = s[i]
                count = 1
                while (i+1) < len(s) and s[i] == s[i+1]:
                    i += 1
                    count += 1
                res.append((str(count), number))
                i += 1
            
            for i in range(len(res)):
                res[i] = res[i][0] + res[i][1]
            
            return "".join(res)
        
        def solution(n):
            if n == 1:
                return "1"
            else:
                return evaluate(solution(n-1))
        
        return solution(n)
        