
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        max = 2**31 - 1
        min = -2**31
        result = 0
        num_len = len(str(x))

        while x:
            if result < min // 10 + 1 or result > max // 10:
                print(result)
                return 0
            
   
            temp = x % 10
            if x < 0 and temp > 0:
                temp -= 10
            result = result * 10 + temp
            x = (x - temp)//10

        return result

