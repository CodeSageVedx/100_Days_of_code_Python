class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        if (dividend==0):
            truncated=0
        elif(dividend>0) and (divisor>0):
            number = float(dividend/divisor)
            integer_part=float(dividend//divisor)
            fractional_part=float(number-integer_part)
            truncated=int(number-fractional_part)
        elif(dividend<0) and (divisor<0):
            number = (dividend/divisor)
            integer_part=float(dividend//divisor)
            fractional_part=float(number-integer_part)
            truncated=int(number-fractional_part)
        elif(dividend<0) or (divisor<0):
            number = float(dividend/divisor)
            integer_part=float(dividend//divisor)
            fractional_part=float(number-integer_part)
            if fractional_part == 0:
                truncated=int(number-fractional_part)
            else:
                truncated=int(number-fractional_part)+1
        
        if truncated > 2147483647:
            return (2147483647)
        elif truncated < -2147483648:
            return (-2147483648)         
        else:
            return truncated