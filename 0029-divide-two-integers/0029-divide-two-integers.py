class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        INT_MAX = 2147483647
        INT_MIN = -2147483648
        if divisor == 0:
            return 0
        
        sign = 1 if (dividend > 0 and divisor > 0) or (dividend < 0 and divisor < 0) else -1
        dividend, divisor = abs(dividend), abs(divisor)
        
        quotient = 0
        for i in range(31, -1, -1):
            if (dividend >= (divisor << i)):
                quotient |= (1 << i)
                dividend -= (divisor << i)
        
        # Avoid multiplication by using conditional sign application
        res = quotient if sign == 1 else -quotient
        
        return min(max(res, INT_MIN), INT_MAX)
