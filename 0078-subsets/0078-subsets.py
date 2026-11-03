class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        def backtrack(start, path):
            # Add a copy of the current path to the result
            result.append(path[:])
            # Explore further subsets
            for i in range(start, len(nums)):
                # Include nums[i] in the current subset
                path.append(nums[i])
                # Recur for the next element
                backtrack(i + 1, path)
                # Backtrack: remove nums[i] from the current subset
                path.pop()
        result = []
        backtrack(0, [])
        return result