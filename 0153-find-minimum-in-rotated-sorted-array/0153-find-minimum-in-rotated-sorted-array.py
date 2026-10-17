class Solution:
    def findMin(self, nums: list[int]) -> int:
        n = len(nums)
        l ,r = 0 , n-1
        while l < r :
            mid = (l + r)//2
            if nums[mid]>nums[r]:
                l = mid+1
            else :
                r = mid 

        return nums[l]
