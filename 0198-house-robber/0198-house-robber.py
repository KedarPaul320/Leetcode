class Solution:
    def rec(self,i,nums,dp):
        # Base case: if the index exceeds the last house, no more money can be robbed
        if i >= len(nums):
            return 0

        # Memoization check: return the precomputed maximum profit if index i was already solved
        if dp[i] != -1 :
            return dp[i]

        # Choice 1: Rob the current house and skip the adjacent house (move to i + 2)
        take = nums[i] + self.rec(i+2,nums,dp)

        # Choice 2: Skip the current house and evaluate the immediate next house (move to i + 1)
        not_take = self.rec(i+1,nums,dp)

        # Store the optimal profit for index i in the memoization table
        dp[i] = max(take,not_take)

        # Return the maximum profit between robbing or skipping the current house
        return dp[i]
    def rob(self, nums: list[int]) -> int:
        # Initialize a memoization array filled with -1 to mark subproblems as unvisited
        dp = [-1] * len(nums)
        # Start the recursive evaluation from the first house at index 0
        return self.rec(0,nums,dp)
