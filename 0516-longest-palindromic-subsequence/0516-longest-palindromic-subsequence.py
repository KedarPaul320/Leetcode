class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        # Store the length of the input string
        n = len(s)
        # Initialize two 1D arrays to represent the current row (dp) and the row below it (prev_dp)
        dp, prev_dp = [0] * n, [0] * n

        # Iterate backwards from the last character to the first to build substrings bottom-up
        for i in range(n - 1, -1, -1):
            # Base case: any single character substring s[i..i] is a palindrome of length 1
            dp[i] = 1
            # Expand the substring's right endpoint j forward from i + 1 to the end
            for j in range(i + 1, n):
                # If outer characters match, add 2 to the longest palindrome inside s[i+1..j-1]
                if s[i] == s[j]:
                    dp[j] = 2 + prev_dp[j - 1]
                # If characters differ, take the max result from excluding either s[i] or s[j]
                else:
                    dp[j] = max(prev_dp[j], dp[j - 1])
            # Copy the current row's results into prev_dp before moving to the next outer index i
            prev_dp = dp[:]

        # Return the result for the full string spanning from index 0 to n - 1
        return dp[n - 1]
