class Solution:
    def loweBound(self,nums,target):
        left = 0 
        right = len(nums)- 1
        ans = len(nums)

        while left<=right :
            mid = (left+right)//2
            if nums[mid] >= target :
                ans = mid 
                right = mid -1
            else :
                left = mid+1
        return ans 
    def searchInsert(self, nums: List[int], target: int) -> int:
        return self.loweBound(nums,target)