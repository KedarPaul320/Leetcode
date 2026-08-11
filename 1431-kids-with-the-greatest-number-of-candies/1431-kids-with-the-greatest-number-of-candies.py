class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxCandies = max(candies)
        result=[]
        for i in candies :
            if (i+extraCandies) >= maxCandies:
                result.append(True)
            elif (i+extraCandies) < maxCandies:
                result.append(False)
        return result


        