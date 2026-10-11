class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        # Initialize the global maximum with the largest single element
        res = max(nums)
        curMin, curMax = 1, 1

        for n in nums:
            if n == 0:
                curMin, curMax = 1, 1
                continue  # Skip to the next number after resetting
            
            # Save the old curMax before it gets overwritten
            tmp = curMax * n  
            
            # Use max() and min() to find the boundaries, and use the correct variable names
            curMax = max(n * curMax, n * curMin, n)
            curMin = min(tmp, n * curMin, n)
            
            # Update the global maximum
            res = max(res, curMax)
            
        return res
