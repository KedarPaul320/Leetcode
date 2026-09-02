class Solution:
    def lowerBound(self,nums,target):
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
    def upperBound(self,nums,target):
            left = 0 
            right = len(nums)- 1
            ans = len(nums)

            while left<=right :
                mid = (left+right)//2
                if nums[mid] > target :
                    ans = mid 
                    right = mid -1
                else :
                    left = mid+1
            return ans 
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        lb = self.lowerBound(nums,target)
        ub = self.upperBound(nums,target)
        if lb == ub :
            #no element 
            return [-1,-1]

        else:
            return [lb,ub-1]

