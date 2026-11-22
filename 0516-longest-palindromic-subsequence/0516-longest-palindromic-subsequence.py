class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        text1 = s 
        text2 = s[::-1]
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
        