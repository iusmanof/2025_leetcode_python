class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman_map = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        result = 0
        tmp_prev = 0
        for i in s:
            result += roman_map.get(i, 0)
            
            if tmp_prev < roman_map.get(i):
                result -= tmp_prev * 2
                
            tmp_prev = roman_map.get(i)
            
        return result