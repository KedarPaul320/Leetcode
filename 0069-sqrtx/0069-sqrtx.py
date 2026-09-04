class Solution:
    def mySqrt(self, x: int) -> int:
        l = 1 
        r = x 
        ans = 0

        while l<=r:
            mid =(l+r)//2
            midSquare = mid*mid
            if midSquare > x :
                r = mid -1 
            else :
                ans = mid 
                l = mid +1
        return ans 