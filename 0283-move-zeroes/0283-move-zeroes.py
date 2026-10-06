class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        insert_pos = 0
        
        # Move all non-zero elements forward
        for i in range(len(nums)):
            if nums[i] != 0:
                # Swap elements
                nums[insert_pos], nums[i] = nums[i], nums[insert_pos]
                insert_pos += 1
        return nums