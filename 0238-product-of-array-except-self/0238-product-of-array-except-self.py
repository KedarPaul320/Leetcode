class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        n = len(nums)
        ans = [] 
        mul = 1 
        count = 0 
        for i in nums :
            if i == 0:
                count += 1 
            else :
                mul *= i 
            
        for i in range (n):
            if nums[i] != 0 :
                if count == 0:
                    ans.append (mul//nums[i])
                else :
                    ans.append(0)
            else :
                if count == 1 :
                    ans.append(mul)
                else :
                    ans.append(0)
        return ans 

        