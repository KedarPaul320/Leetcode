class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            
            # 1. Check if the mid element is our target
            if nums[mid] == target:
                return mid 
            
            # 2. Check if the left half is sorted
            elif nums[left] <= nums[mid]:
                # If target is inside the sorted left half, narrow search to the left
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            
            # 3. Otherwise, the right half must be sorted
            else:
                # If target is inside the sorted right half, narrow search to the right
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1 

        # Target was not found in the array
        return -1
