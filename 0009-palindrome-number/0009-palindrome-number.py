class Solution:
    def isPalindrome(self, x: int) -> bool:
        temp = x
        new_num = 0 
        while temp>0:
            rem = temp %10
            temp = temp//10
            new_num = new_num*10 + rem 
        
        return new_num == x 
            
        