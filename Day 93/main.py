# Combinations
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        def bt(idx, comb):
            if len(comb) == k:
                ans.append(comb[:])
                return
            for i in range(idx, n + 1):
                comb.append(i)
                bt(i + 1, comb)
                comb.pop()
        bt(1, [])
        return ans