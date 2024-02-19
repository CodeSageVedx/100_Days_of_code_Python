# Combination Sum
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []

        def dfs(i, curr, total):
            # If the total sum equals the target, we've found a valid combination
            if total == target:
                result.append(curr.copy())
                return
            # If the index is out of bounds or total sum exceeds the target, stop exploring this path
            if i >= len(candidates) or total > target:
                return

            # Include the current candidate in the combination
            curr.append(candidates[i])
            # Explore further combinations with the current candidate
            dfs(i, curr, total + candidates[i])
            # Backtrack: remove the last candidate to explore combinations without it
            curr.pop()
            # Explore combinations without the current candidate
            dfs(i + 1, curr, total)

        # Start DFS traversal from index 0 with an empty current combination and total sum 0
        dfs(0, [], 0)
        return result