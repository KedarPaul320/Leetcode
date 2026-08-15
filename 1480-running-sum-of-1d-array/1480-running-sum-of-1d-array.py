class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        ans = []
        n = len(nums)
        ans.append(nums[0])
        for i in range (1,n):
            sum = ans[i-1]+nums[i]
            ans.append(sum)
        return ans 
        