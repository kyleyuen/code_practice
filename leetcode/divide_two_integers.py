class Solution:
    # @return an integer
    def divide(self, dividend, divisor):
        if divisor == 0:
            return 0

        negative = False
        if (dividend>0) and (divisor<0):
            negative = True
            divisor = -divisor
        elif (dividend<0) and (divisor>0):
            negative = True
            dividend = -dividend
        elif (dividend<0) and (divisor<0):
            dividend = -dividend
            divisor = -divisor

        result = 0
        while dividend > 0:
            quotient, dividend = self.do_divide(dividend, divisor)
            result += quotient

        if negative:
            result = -result
        return result


    def do_divide(self, dividend, divisor):
        if dividend < divisor:
            return (0, 0)
        
        dividend -= divisor
        quotient = 1
        while dividend >= divisor:
            dividend -= divisor
            quotient += quotient
            divisor += divisor
        return (quotient, dividend)


s = Solution()
print s.divide(-1, -1)