class Solution:
    def minSteps(self, n: int) -> int:
        if n == 1:
            return 0
            
        cache = {}
        
        def helper(count, paste):
            if count == n:
                return 0
            if count > n:
                return float('inf')
            if (count, paste) in cache:
                return cache[(count, paste)]
            
            # Option 1: Just paste the current clipboard
            res1 = 1 + helper(count + paste, paste)
            
            # Option 2: Copy all and paste (only if we are changing the count)
            res2 = 2 + helper(count + count, count) if count != paste else float('inf')
            
            cache[(count, paste)] = min(res1, res2)
            return cache[(count, paste)]
        
        # Start at 1 'A', with 1 'A' already in the clipboard (takes 1 operation: Copy)
        return 1 + helper(1, 1)
