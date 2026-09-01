class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        count = {}
        for i in nums :
            if i not in count :
                count[i] = 1 
            else :
                count[i] +=1 
        target_value = min(count.values())
        results=[]
        for k, v in count.items():
            if v == target_value:
                results.append(k)
        return results