class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        sum = ""
        for i in digits :
            sum += str(i) 
        new_num = str(int(sum)+1)
        digits = [int(i) for i in new_num]
        return digits


        