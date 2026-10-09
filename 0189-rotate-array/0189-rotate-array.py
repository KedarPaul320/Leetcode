class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k %= n  # Handles cases where k is greater than the length of nums
        
        # Modify the array in-place using slice assignment
        nums[:] = nums[n - k:] + nums[:n - k]