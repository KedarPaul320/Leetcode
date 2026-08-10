class Solution:
    def countDigits(self, num: int) -> int:
        temp = num
        c = 0
        while temp!=0:
            rem = temp%10
            if num % rem == 0 :
                c+=1
            temp = temp//10
        return c 
        

        