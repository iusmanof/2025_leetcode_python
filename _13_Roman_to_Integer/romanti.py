class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        dict_roman_to_item = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
                
        i = 0
        result = 0
        while i < len(s): 
            j = i + 1
            if j < len(s) and dict_roman_to_item[s[i]] < dict_roman_to_item[s[j]]:
                result+=dict_roman_to_item[s[j]] - dict_roman_to_item[s[i]]
                i+=2
            else:
                result += dict_roman_to_item[s[i]]
                i+=1
        return result
        
        