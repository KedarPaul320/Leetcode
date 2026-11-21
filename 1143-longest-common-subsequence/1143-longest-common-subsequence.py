class Solution:
    def rec(self, i, j, text1, text2, dp):
        # Base case: if either pointer reaches the end of its string, no more common characters exist
        if i >= len(text1) or j >= len(text2):
            return 0
        
        # Fix 1: Compare against integer -1, not string "-1"
        # Memoization check: return the cached result if state (i, j) has already been solved
        if dp[i][j] != -1:
            return dp[i][j]
            
        # If characters match, count 1 and advance both string pointers diagonally
        if text1[i] == text2[j]:
            ans = 1 + self.rec(i + 1, j + 1, text1, text2, dp)
        # If characters differ, explore skipping one character from either string and take the maximum
        else:
            # Fix 2: Use max() instead of creating a tuple with a comma
            ans = max(self.rec(i, j + 1, text1, text2, dp), self.rec(i + 1, j, text1, text2, dp))
            
        # Store the calculated optimal length for state (i, j) in the DP table
        dp[i][j] = ans
        # Return the computed result for the current state
        return dp[i][j]

    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # Initialize a 2D memoization table of size len(text1) x len(text2) filled with -1
        dp = [[-1 for _ in range(len(text2))] for _ in range(len(text1))]
        # Start the recursive search from index 0 of both strings
        return self.rec(0, 0, text1, text2, dp)
