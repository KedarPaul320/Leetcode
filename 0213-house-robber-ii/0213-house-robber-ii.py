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
        n = len(nums)
        
        # Edge case: if there is only one house, rob it
        if n == 1:
            return nums[0]
        
        # Scenario 1: Exclude the last house (consider indices 0 to n-2)
        nums1 = nums[:-1]
        dp1 = [-1] * len(nums1)
        profit1 = self.rec(0, nums1, dp1)
        
        # Scenario 2: Exclude the first house (consider indices 1 to n-1)
        nums2 = nums[1:]
        dp2 = [-1] * len(nums2)
        profit2 = self.rec(0, nums2, dp2)
        
        # Return the maximum profit from the two valid scenarios
        return max(profit1, profit2)