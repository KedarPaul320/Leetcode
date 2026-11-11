class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        # 1. n must be greater than 0
        # 2. n & (n - 1) == 0 checks if n is a power of 2
        # 3. n & 0xaaaaaaaa == 0 ensures the single set bit is at an odd position (0-indexed: 0, 2, 4, ...)
        return n > 0 and (n & (n - 1)) == 0 and (n & 0xaaaaaaaa) == 0
