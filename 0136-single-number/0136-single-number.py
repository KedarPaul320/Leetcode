class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        count = {}
        for i in nums :
            if i not in count :
                count[i] = 1 
            else :
                count[i] +=1 
        target_value = min(count.values())
        return next(k for k, v in count.items() if v == target_value)

        

        