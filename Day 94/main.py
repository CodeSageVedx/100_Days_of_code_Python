# Subsets
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        lst = [[]]
        for i in range(1, len(nums) + 1):
            ans = list(itertools.combinations(nums, i))
            lst.extend([list(comb) for comb in ans])
        return lst