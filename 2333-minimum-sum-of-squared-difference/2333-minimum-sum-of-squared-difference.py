class Solution:
    def minSumSquareDiff(self, nums1: list[int], nums2: list[int], k1: int, k2: int) -> int:
        # Combine the total operation budget
        k = k1 + k2
        
        # Calculate absolute element-wise differences
        diffs = [abs(n1 - n2) for n1, n2 in zip(nums1, nums2)]
        max_diff = max(diffs)
        
        # Base case: arrays are already identical
        if max_diff == 0:
            return 0
            
        # Initialize a bucket-sort array to track difference frequencies
        freq = [0] * (max_diff + 1)
        for d in diffs:
            freq[d] += 1
            
        # Greedily flatten the largest differences downward
        for d in range(max_diff, 0, -1):
            if freq[d] == 0:
                continue
                
            # Cap operations by available counts or remaining budget
            take = min(freq[d], k)
            
            # Shift processed differences to the next level down
            freq[d] -= take
            freq[d - 1] += take
            k -= take
            
            # Terminate early once budget is spent
            if k == 0:
                break
                
        # Sum up the squared values of the final differences
        return sum(freq[d] * (d ** 2) for d in range(1, max_diff + 1))
