class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        prd = 1
        summ = 0 
        while n!=0:
            rem = n%10
            prd = prd * rem 
            summ = summ + rem 
            n = n//10
        return (prd-summ)

        