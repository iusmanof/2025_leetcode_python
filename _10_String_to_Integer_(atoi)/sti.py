class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        INT_MIN = -2**31
        INT_MAX = 2**31 - 1
        ifMinus=False
        i = 0
        
        s = s.strip()
        if not s:
            return 0
        if s[0] in ["-","+"]:
            ifMinus= s[0] == "-"
            i+=1
            
        result = ""
        while i < len(s) and s[i].isdigit():
            result += s[i]
            i+=1
            
        if not result:
            return 0
                    
        number = int(result)  
        number = -number if ifMinus else number 
        

        return max(INT_MIN, min(number, INT_MAX))