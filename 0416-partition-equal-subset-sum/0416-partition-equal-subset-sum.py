class Solution:
    def rec (self, i , sums, nums ,total,dp):
        # Base case 1: current subset sum exceeded half the total, so this path is invalid
        if sums > (total//2) :
            return False
        # Base case 2: exact half-sum reached, meaning the remaining elements form the other half
        elif sums == (total//2) :
            return True 
        # Base case 3: reached the end of the array without hitting the target half-sum
        elif i == len(nums):
            return False

        # Memoization check: return cached result if this (index, current sum) state was already solved
        if dp[i][sums] != -1 :
            return dp[i][sums]

        # Choice 1: Include the current number in the subset sum and move to the next index
        take = self.rec(i+1 , sums+nums[i] , nums,total,dp)

        # Choice 2: Exclude the current number from the subset sum and move to the next index
        not_take = self.rec(i+1 , sums, nums,total,dp)

        # Store True in the DP table if either choice leads to a valid equal partition
        dp[i][sums] = take or not_take

        # Return the computed boolean result for the current state
        return dp[i][sums]

    def canPartition(self, nums: list[int]) -> bool:
        # Get the total number of elements in the array
        n = len(nums)

        # Edge case: a single element cannot be split into two non-empty subsets
        if n == 1 :
            return False
        
        # Calculate total sum; if odd, it cannot be divided into two equal integer subsets
        total = sum(nums)
        if total%2 == 1 :
            return False

        # Initialize a 2D memoization table of size n x (half_total + 1) with -1
        dp = [[-1 for j in range((total//2)+1)] for i in range(n)]

        # Start the recursive search from index 0 with an initial subset sum of 0
        return self.rec(0,0,nums,total,dp)
