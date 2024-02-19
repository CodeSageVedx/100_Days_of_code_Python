# Combination Sum 2
from collections import Counter
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
            
        def dfs(nums,remaining,start_index,path):

            if remaining==0:
                result.append(path[:])
                return
            
            
            for i in range(start_index,len(nums)):
                #Dedupe
                if i>start_index and nums[i]==nums[i-1]:
                    continue
                #Prune
                if nums[i]>remaining:
                    break

                dfs(nums,remaining-nums[i],i+1,path+[nums[i]])


        candidates.sort()
        result=[]
        dfs(candidates,target,0,[])
        return result