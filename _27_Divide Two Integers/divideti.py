class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        INT_MAX = 2**31-1
        INT_MIN = -2**31

        if divisor == 0:
            return INT_MAX
        
        if dividend == INT_MIN and divisor == -1:
            return INT_MAX
        
        negative = (dividend < 0 ) != (divisor < 0)
        dividend = abs(dividend)
        divisor = abs(divisor)

        result = 0
        while dividend >= divisor:
            temp_divisor = divisor
            num_divisors = 1

            while dividend >= (temp_divisor << 1):
                temp_divisor <<= 1
                num_divisors <<= 1 
            
            dividend -= temp_divisor
            result += num_divisors

        if negative:
            result = -result


        if result < INT_MIN:
            return INT_MIN
        if result > INT_MAX:
            return INT_MAX

        return result
