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
        # Store the lengths of both input strings
        n, m = len(text1), len(text2)
        # Initialize DP table with 0s so base cases (row 0 and col 0) are 0
        dp = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
        
        # Iterate through each character prefix of text1
        for i in range(1, n + 1):
            # Iterate through each character prefix of text2
            for j in range(1, m + 1):
                # If characters match, extend the diagonal subproblem result by 1
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                # If characters differ, carry forward the maximum LCS from either top or left cell
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
                    
        # Return the bottom-right cell containing the final LCS length for the full strings
        return dp[n][m]
