class Solution:
    def nextPermutation(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        N = len(nums)
        pivot = 0

        # 1. Find the first decreasing element from the right
        for i in range(N - 1, 0, -1):
            if nums[i - 1] < nums[i]:
                pivot = i 
                break  
                
        # If no pivot found, the array is in descending order; reverse it
        if pivot == 0:
            nums.reverse()
            return 

        # 2. Find the successor to the pivot value
        swap = N - 1 
        while nums[pivot - 1] >= nums[swap]: 
            swap -= 1 

        # 3. Swap them
        nums[swap], nums[pivot - 1] = nums[pivot - 1], nums[swap]
        nums[pivot:] = sorted(nums[pivot:])

        # # 4. Reverse the suffix in-place (O(N) instead of O(N log N) sort)
        # left = pivot
        # right = N - 1
        # while left < right:
        #     nums[left], nums[right] = nums[right], nums[left]
        #     left += 1
        #     right -= 1
